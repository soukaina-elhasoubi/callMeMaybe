import sys
import os
from llm_sdk import Small_LLM_Model

sys.path.insert(0, os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    '..',
    'llm_sdk'
    )))


def main():
    sc = Small_LLM_Model()
    lis = sc.encode("what is the capital of france ?").tolist()[0]
    capital = ['paris', 'rabat', 'qahira', 'madrid']
    captial_ids = []

    for i in capital:
        captial_ids.append(sc.encode(i).tolist()[0][0])

    ids = []
    pos = 0
    while True:
        logits = sc.get_logits_from_input_ids(lis)
        id = max(range(len(logits)), key=logits.__getitem__)
        # best_score = logits[id]
        lis.append(id)
        ids.append(id)
        if pos == 50:
            break
        pos += 1
    # print(ids)
    print(sc.decode(ids))


#     st = sc.decode(lis)
#     tt = sc.encode("Hello girl 12 5 1 2").tolist()[0]
#     es = sc.encode("                       ").tolist()[0]
#     es_one = sc.encode(" ").tolist()[0]
#     es_two = sc.encode("  ").tolist()[0]
#     es_3 = sc.encode("   ").tolist()[0]
#     tab = sc.encode("   ").tolist()[0]
#     es4 = sc.encode("    ").tolist()[0]
#     tab2 = sc.encode("      ").tolist()[0]
#     inf = sc.decode([188])

#     des = sc.decode([154])
#     fr = sc.decode([82])
#     print(inf)
#     print(des)
#     print(fr)
#     print(lis)
#     print(st)
#     print(tt)
#     print(es)
#     print(es_one)
#     print(es_two)
#     print(es_3)
#     print(tab)
#     print(tab2)
#     print(es4)
main()
