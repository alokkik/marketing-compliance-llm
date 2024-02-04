from llama_index.callbacks import OpenAIFineTuningHandler
from llama_index.finetuning import OpenAIFinetuneEngine
import pickle

def dump(obj, file_name):
    with open(file_name, "wb") as f:
        pickle.dump(obj, f)
    print(f"Object saved to {file_name}")

def fine_tune(model, data_file):
    finetuning_handler = OpenAIFineTuningHandler()

    finetuning_handler.save_finetuning_events("data/fine_tuning_events.jsonl")

    finetune_engine = OpenAIFinetuneEngine(
        model,
        data_file
    )

    finetune_engine.finetune()
    ft_llm = finetune_engine.get_finetuned_model(temperature=0.3)
    
    return ft_llm