# Therapy Chatbot Data Translation and Flowchart Framework

This repository provides a framework for processing, translating, and analyzing chatbot session data related to therapy sessions. The goal is to enable prompt-based translations, dataset merging, flowchart creation, and result analysis to support the development of a multilingual therapy chatbot. The system primarily focuses on translating English text into Persian and structuring dialogue flowcharts for chatbot development.

## Project Structure

- **Dataset**: Contains various data files related to therapy sessions and flowcharts used for chatbot training and analysis.
  - **HOPE_therapy_session_transcripts**: Raw session transcripts labeled by session number, available in CSV format for individual sessions.
  - `combined_transcripts.csv` and `combined_transcripts_translated.csv`: Consolidated session transcripts for easier processing, with translated versions for non-English texts.
  - `train.csv` and `result.csv`: Additional datasets prepared for training and evaluation.
  - `chatbot_flowchart_final_corrected.xlsx` and `chatbot_flowchart_final_corrected_translated_full_manual.xlsx`: Flowchart files outlining chatbot decision paths, with translated and corrected versions for Persian language support.

- **Prompts**: A folder to store prompt files if additional prompt-based NLP models are integrated.

- **Results**: Stores results of data analysis and model predictions.
  - `Results_Analysis.xlsx`: Analysis of classification results and performance metrics for the translated sessions.

- **Scripts**: Core Python scripts and notebooks for data processing and translation.
  - `DatasetCreator.py`: Utility script for creating and merging datasets from session transcripts.
  - `FlowChartCreator.py`: Generates flowcharts for chatbot conversations, helping to define conversational paths based on session data.
  - `FlowChartTranslator.py`: Translates flowchart states, questions, and responses into Persian, creating a bilingual reference for chatbot training.
  - `merge_dataset.ipynb`: Notebook to merge multiple session datasets into a single file for streamlined processing.
  - `SAT_Translate.ipynb`: Uses Facebook's SeamlessM4T model for bulk translation of session data into Persian.
  - `Aya_Translator.ipynb`: Implements a prompt-based translation system using a pre-trained model from Cohere for translating selected columns of session data.

- **Translator**: Contains additional notebooks and scripts related to translation tasks.
  - `Aya_Translator.ipynb`: Notebook implementing a 4-bit quantized translation model for Persian-English translation, optimized for memory efficiency.

## Key Features

- **Data Translation**: Provides translation from English to Persian for therapy session data, ensuring multilingual support for chatbot interactions. Utilizes models like Cohere's GPT-based language model and Facebook’s SeamlessM4T for translation.
- **Flowchart Creation and Translation**: Supports creation and translation of conversation flowcharts to guide chatbot dialogue paths. This is crucial for maintaining structured therapy interactions in Persian and English.
- **Batch Processing and Translation**: Uses `Aya_Translator.ipynb` and `SAT_Translate.ipynb` for batch processing of data, enabling large-scale translation of session transcripts while preserving the conversational context.
- **Result Analysis**: Includes tools to evaluate the translation quality and analyze conversational data, helping improve chatbot responses through structured feedback loops.

## Setup Instructions

1. **Clone the repository**:

   ```bash
   git clone https://github.com/ShayanSalehi81/InternshipProject
   cd InternshipProject
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Model Setup**:
   - Download and configure models for translation as per instructions in the notebooks `Aya_Translator.ipynb` and `SAT_Translate.ipynb`.
   - Ensure access to Hugging Face and Cohere API tokens if necessary for model loading.

4. **Prepare Data**:
   - Add raw session transcript files to `Dataset/HOPE_therapy_session_transcripts`.
   - Run `merge_dataset.ipynb` to consolidate and preprocess data for batch translation.

## Usage

### Translating Session Data

1. **Aya_Translator**: 
   - Open `Aya_Translator.ipynb` and execute the notebook to translate specified columns (e.g., Context, Response) from English to Persian.
   - The translated text will be saved back to `result.csv` or another specified file.

2. **SAT_Translate**:
   - Use `SAT_Translate.ipynb` to perform bulk translation of session transcripts with the SeamlessM4T model. This notebook translates entire transcript files and outputs them to `combined_transcripts_translated.csv`.

### Creating and Translating Flowcharts

- **FlowChartCreator**:
  - Run `FlowChartCreator.py` to create a structured flowchart from the session transcripts, organizing states, questions, and possible paths for a chatbot flow.
  
- **FlowChartTranslator**:
  - Use `FlowChartTranslator.py` to translate flowchart entries into Persian. The script ensures that all conversational paths, exercises, and prompts are bilingual, which is essential for building a multilingual chatbot.

### Analyzing Results

- Open `Results_Analysis.xlsx` to review analysis results for translations and chatbot responses.
- Additional analysis scripts can be added to the `Results` directory for future expansion or specialized metrics.

## Example Workflow

1. **Data Preparation**: Run `DatasetCreator.py` to compile session data into structured datasets like `train.csv` and `result.csv`.
2. **Translation**: Execute `Aya_Translator.ipynb` or `SAT_Translate.ipynb` to translate dataset columns or entire transcripts.
3. **Flowchart Generation and Translation**: Generate flowcharts with `FlowChartCreator.py` and translate them using `FlowChartTranslator.py`.
4. **Analysis**: Use `Results_Analysis.xlsx` to validate and analyze translated responses for quality control.

## Future Enhancements

- **Advanced Language Support**: Integrate additional languages to support broader audiences.
- **Enhanced Prompt Design**: Experiment with in-context examples and prompt engineering for better translation fidelity in therapy settings.
- **Interactive Chatbot Integration**: Develop a real-time, interactive chatbot that leverages the translated data for live therapy sessions.

## License

This project is licensed under the MIT License.

## Contributing

Contributions are welcome! Please submit issues, feature requests, or pull requests to help improve the framework.