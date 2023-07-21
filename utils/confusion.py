import numpy as np

# Entropy-based Analysis (common threshold: 1.0)
def calculate_entropy(probabilities):
    return -np.sum([p * np.log2(p) for p in probabilities if p > 0])

# margin of victory (common threshold: > 0.5)
def calculate_mov(probabilities):
    sorted_probs = sorted(probabilities, reverse=True)
    return sorted_probs[0] - sorted_probs[1]

NEO_CLASSES = {'biological': 0, 'cardboard': 1, 'glass': 2, 'metal': 3, 'paper': 4, 'plastic': 5, 'trash': 6} # XL model for bio + trash
TRINITY_CLASSES = {'cardboard': 0, 'glass': 1, 'metal': 2, 'paper': 3, 'plastic': 4, 'trash': 5} # regular model for everything else

MORPHEUS_CLASSES = {
    'biological1': 0, 
    'cardboard1': 1, 
    'glass1': 2, 
    'metal1': 3, 
    'paper1': 4, 
    'plastic1': 5, 
    'trash1': 6,
    'cardboard2': 7, 
    'glass2': 8, 
    'metal2': 9, 
    'paper2': 10, 
    'plastic2': 11, 
    'trash2': 12
}

def get_confusion_level(data):
    morpheus_preds = data['result'][0]['probabilities'][0]
    neo_preds = data['result'][0]['m1_confidence']
    trinity_preds = data['result'][0]['m2_confidence']
    
    morpheus_entropy = calculate_entropy(morpheus_preds)
    morpheus_mov = calculate_mov(morpheus_preds)
    
    neo_entropy = calculate_entropy(neo_preds)
    neo_mov = calculate_mov(neo_preds)
    
    trinity_entropy = calculate_entropy(trinity_preds)
    trinity_mov = calculate_mov(trinity_preds)
    
    # format a string to display the results
    output = f"""
    
    #####################
    ##
    ## Morpheus:
    ## 
    ## prediction: {MORPHEUS_CLASSES[morpheus_preds.index(max(morpheus_preds))]} -> {max(morpheus_preds) * 100}%
    ## entropy: {morpheus_entropy}
    ## mov: {morpheus_mov}
    ##
    #####################
    
    #####################
    ##
    ## Neo:
    ##
    ## prediction: {NEO_CLASSES[neo_preds.index(max(neo_preds))]} -> {max(neo_preds) * 100}%
    ## entropy: {neo_entropy}
    ## mov: {neo_mov}
    ##
    #####################
    
    #####################
    ##
    ## Trinity:
    ## 
    ## predction: {TRINITY_CLASSES[trinity_preds.index(max(trinity_preds))]} -> {max(trinity_preds) * 100}%
    ## entropy: {trinity_entropy}
    ## mov: {trinity_mov}
    ##
    #####################
    
    """
    
    print(output)