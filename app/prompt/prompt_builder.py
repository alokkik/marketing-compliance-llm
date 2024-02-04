from llama_index.prompts import PromptTemplate

class PromptBuilder:
    def __init__(self, template):
        self.template = template

    def build_prompt(self, **kwargs):
        qa_template = PromptTemplate(self.template)
        return qa_template.format(**kwargs)
