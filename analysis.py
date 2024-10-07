import pandas as pd
from scipy.stats import pearsonr
import numpy as np
import matplotlib.pyplot as plt

def create_freq_table(word_freq):
    top_words=word_freq[:100]
    df = pd.DataFrame(top_words, columns=['word','Frequency'])
    return df


def zipf_law_analysis(sorted_words,top_n='',lang='English'):
    
    ranks = np.arange(1, len(sorted_words) + 1) 
    frequencies = np.array([freq for _, freq in sorted_words])
    C = frequencies[0]  # Most frequent word's frequency as the constant
    zipf_frequencies = C / ranks
    
    print(f"{'Rank':<10} {'Word':<15} {'Actual Freq':<15} {'Zipf Predicted Freq'}")
    for i in range(top_n):
        word, freq = sorted_words[i]
        zipf_freq = zipf_frequencies[i]
        print(f"{i+1:<10} {word:<15} {freq:<15} {zipf_freq:.2f}")
  

    plt.figure(figsize=(10, 5))
    plt.loglog(ranks[:top_n], frequencies[:top_n], label='Actual Frequencies', marker='o')
    plt.loglog(ranks[:top_n], zipf_frequencies[:top_n], label="Zipf's Law Prediction", linestyle='--', marker='x')
    plt.xlabel('Rank (r)')
    plt.ylabel('Frequency (f)')
    plt.title(f'Zipf\'s Law Analysis {lang}')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    

    return ranks, frequencies
    
def calculate_fr(sorted_words,output_file):
    top_25=sorted_words[:25]
    fr_values = [(word, freq * rank, freq, rank) for rank, (word, freq) in enumerate(top_25, 1)]
    
    df = pd.DataFrame(fr_values, columns=['Word', 'f*r', 'Frequency', 'Rank'])
    df.to_csv(output_file, index=False)
    
    
def Correlation(ranks,frequencies):
    return pearsonr(ranks,frequencies)