from llm_sdk.llm_sdk import Small_LLM_Model

def main():
    sc  = Small_LLM_Model()
    lis = sc.encode("soukaina").tolist()[0]
    print(lis)
main()