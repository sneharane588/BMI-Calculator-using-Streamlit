import streamlit as st

st.title('BMI 💪 Calculator')

weight = st.number_input('Weight(in kg): ')
status = st.radio('Height format: ', ('cms', 'meters', 'feet'))

if(status == 'cms'):
  height = st.number_input('Height: ')
  try:
    bmi = weight / ((height/100)**2)
  except:
    st.text('Enter a valid height input')

elif(status == 'meters'):
  height = st.number_input('Height: ')
  try:
    bmi = weight / (height **2)
  except:
    st.text('Enter a valid height input')

else:
  height = st.number_input('Height: ')
  try:
    bmi = weight / ((height/3.28)**2)
  except:
    st.text('Enter a valid height input')

if(st.button('Calculate BMI: ')):
  st.text('Your BMI is {:.2f}'.format(bmi))
  st.text('\n\nResulted BMI Interpretation: \n')
   # give the interpretation of BMI index
  if(bmi < 16):
    st.error("You are Extremely Underweight")
  elif(bmi >= 16 and bmi < 18.5):
    st.warning("You are Underweight")
  elif(bmi >= 18.5 and bmi < 25):
    st.success("You are Healthy")        
  elif(bmi >= 25 and bmi < 30):
    st.warning("You are Overweight")
  elif(bmi >= 30):
     st.error("Extremely Overweight")
