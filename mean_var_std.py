import numpy as np

def calculate(list):
  
  try:
      #converting list into 3X3 matrix	
      num_array = np.array(list).reshape(3,3)
        
      #calculating mean across Row, column and mean of matrix
      mean_row = np.mean(num_array,axis = 0).tolist() 
      mean_col =np.mean(num_array,axis = 1).tolist()
      mean_val = np.mean(num_array)
      #calculating variance across rows, column and variance of matrix
      vari_row = np.var(num_array,axis = 0).tolist()
      vari_col = np.var(num_array,axis = 1).tolist()
      variance = np.var(num_array)
      #standard deviation calculating standard deviation across Row, column and standard deviation of matrix
      sd_row = np.std(num_array,axis = 0).tolist() 
      sd_col = np.std(num_array,axis = 1).tolist()
      sd =  np.std(num_array)
      #calculating maximum across Row, column and maximun of matrix
      max_row = np.max(num_array,axis = 0).tolist() 
      max_col = np.max(num_array,axis = 1).tolist() 
      maximum = np.max(num_array)
      #calculating minimum across Row, column and minimum of matrix
      min_row = np.min(num_array,num_array,axis=0).tolist() 
      min_col = np.min(num_array,axis=1).tolist() 
      minimum = np.min(num_array)
      #calculating sum across Row, column and sum of matrix
      sum_row = np.sum(num_array,axis=0).tolist()
      sum_col = np.sum(num_array,axis=1).tolist()
      sum_val = np.sum(num_array)
      #converting the result into a dictionary value  
      calulation = {'mean': [mean_row, mean_col, mean_val],
             'variance': [vari_row, vari_col, variance],
             'standard deviation': [sd_row, sd_col, sd],
             'max' : [max_row, max_col, maximum],
             'min' : [min_row, min_col, minimum],
             'sum' : [sum_row, sum_col, sum_val]
             }
      return calulation
  except ValueError:
    print('List must contain nine numbers.')