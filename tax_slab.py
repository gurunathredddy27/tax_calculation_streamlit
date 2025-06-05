'''
The tax_slab.py scripts has tax calculation according to old and new regime
The system will support functionalites like calculating Tax, Standard deduction, Life Insurance Premium

==================  ==================================================
Function                  Description
==================  ==================================================
title()                   Title of the project(ax Calculation Project)
old_tax_regime():         Calculate the tax according to Old Regime
new_tax_regime():         calculate the tax according to New Regime

'''

import streamlit as st
import pandas as pd
import datetime
import matplotlib.pyplot as plt

st.title('💰Tax Calculation Project')
# st.markdown('---')
# st.write('## Tax calculation')
# st.markdown("<h1>Tax calculation<h1>", unsafe_allow_html=True)



# Sidebar
st.sidebar.write('## Basic details')
present_year = datetime.datetime.now().year
year = list(range(present_year - 3, present_year+3))
select_year = st.sidebar.selectbox('Select a Year:', year)

gender = st.sidebar.selectbox('Gender:',('Male','Female','Other'))
age = st.sidebar.selectbox('Age: ',('Below 60', 'Equal or Above 60', 'Equal or Above 80'))
resident = st.sidebar.selectbox('Residential Status:',('Resident','Non-Resident'))
   
st.sidebar.write('## Income & Deductions details')
income = st.sidebar.number_input('Enter your total income (₹):', min_value=0, step= 50000)
life_insurance=st.sidebar.number_input('Life Insurance Premium:', min_value=0)
for_parents = st.sidebar.number_input('For parents above 60yrs:', min_value=0)
tax = 0


#calculation
# Old Tax
def old_tax_regime(income,life_insurance):
    tax = 0
    new_tax = 0
    standard_deduction = 25000
    # insu_parents = 0
    # insu_medical = 0

    if income <=250000:
        tax = 0
        return tax
    elif income <=500000:
        if life_insurance > 0:
            new_tax = (income - standard_deduction - life_insurance) * 0.05
            return new_tax
        else:
            tax = (income - standard_deduction- 250000) * 0.05
            return tax
    elif income <= 1000000:
        if life_insurance > 0:
            new_tax = (income - standard_deduction - life_insurance) * 0.05
            return new_tax
        else:
            tax = (250000 * 0.05) +(income - standard_deduction -500000) * 0.20
            return tax
    else:
        if life_insurance > 0:
            new_tax = (250000 * 0.05) + (500000 * 0.20)+ (income - standard_deduction -life_insurance- 1000000) * 0.30
            return new_tax
        else:
            tax = (250000 * 0.05) + (500000 * 0.20) + (income - 1000000) * 0.30
            return tax


#New Tax
def new_tax_regime(income, life_insurance):
    tax = 0
    new_tax = 0
    standard_deduction = 75000
    # taxable_income = income-life_insurance-standard_deduction
    if income <= 400000:
        tax = 0
        return tax
    elif income <= 800000:
        if life_insurance > 0:
            new_tax = (income - life_insurance- standard_deduction- 400000) * 0.05
            return new_tax
        else:
            tax = (income - standard_deduction-400000) * 0.05
            return tax
    elif income <= 1200000:
        if life_insurance > 0:
            new_tax =(400000 * 0.05) + (income - standard_deduction-life_insurance- 800000) * 0.10
            return new_tax
        else:
            tax = (400000 * 0.05) + (income - standard_deduction- 800000) * 0.10
            return tax
    elif income <= 1600000:
        if life_insurance > 0:
            new_tax =(400000 * 0.05) + (400000 * 0.10) +  (income - standard_deduction-life_insurance- 1200000) * 0.15
            return new_tax
        else:
            tax = (400000 * 0.05) + (400000 * 0.10) +(income - standard_deduction- 1200000) * 0.15
            return tax
    elif income <= 2000000:
        if life_insurance > 0:
            new_tax =(400000 * 0.05) + (400000 * 0.10)+ (400000 * 0.15) +  (income - standard_deduction-life_insurance- 1600000) * 0.20
            return new_tax
        else:
            tax = (400000 * 0.05) + (400000 * 0.10)+ (400000 * 0.15) +(income - standard_deduction- 1600000) * 0.20
            return tax
    elif income <= 2400000:
        if life_insurance > 0:
            new_tax =(400000 * 0.05) + (400000 * 0.10)+ (400000 * 0.15)+ (400000 * 0.20) +  (income - standard_deduction-life_insurance- 2000000) * 0.25
            return new_tax
        else:
            tax = (400000 * 0.05) + (400000 * 0.10)+ (400000 * 0.15) + (400000 * 0.20)+(income - standard_deduction- 2000000) * 0.25
            return tax
    else:
        if life_insurance > 0:
            new_tax =(400000 * 0.05) + (400000 * 0.10)+ (400000 * 0.15)+ (400000 * 0.20) + (400000 * 0.25)+  (income - standard_deduction-life_insurance- 2400000) * 0.30
            return new_tax
        else:
            tax = (400000 * 0.05) + (400000 * 0.10)+ (400000 * 0.15) + (400000 * 0.20)+ (400000 * 0.25) +(income - standard_deduction- 2400000) * 0.30
            return tax


# Main logic---
st.markdown('---')
st.write('### Select your tax regime:')

col1, col2 = st.columns(2)
old_clicked = col1.button('**Old Regime**')
new_clicked = col2.button('**New Regime**')
# st.markdown('---')

if income>0:
    option=0
    standard_deduction = 25000
    if old_clicked:
        option = "Old"
        tax = old_tax_regime(income, life_insurance)
        # st.write('You selected **"Old Regime**"')
        st.success(f"Under **Old Regime**, your total tax payable is ₹ {tax:,.2f}💸:thumbsup:")
        
    elif new_clicked:
        option = "New"
        tax = new_tax_regime(income, life_insurance)
        # st.write('You selected **"New Regime**"')
        st.success(f"Under **New Regime**, your total tax payable is ₹ {tax:,.2f}💸:thumbsup:")
        standard_deduction = 75000
    else:
        st.info("Please select a tax regime to see your tax calculation.")

    take_home = income - tax
    taxable_income = income - standard_deduction - life_insurance


    # Tax Summary
    st.markdown('---')
    st.subheader('Tax summary:')

    col1, col2 = st.columns(2)
    with col1:
        st.write(f"**→ Tax Regime Selected:** '{option} Regime'" ) 
        st.write(f'**→ Gross Income:** ₹ {income:,.2f}')
        st.write(f"**→ Taxable Income** {taxable_income:,.2f}")
        st.write(f'**→ Total Tax Payable:** ₹ {tax:,.2f}')
    with col2:
        # st.markdown("<br>", unsafe_allow_html= True)
        st.write(f'**→ Standard Deduction:** {standard_deduction:,.2f}')
        st.write(f'**→ Total Deduction:** ₹ {life_insurance:,.2f}')
        st.write(f'**→ Take-Home Salary (After-Tax)** ₹ {take_home:,.2f}')
    import streamlit as st



    
    
    # Ploting 
    st.markdown('---')
    total_decuction = life_insurance+standard_deduction
    st.subheader('Visual Comparision: ')
    fig, ax = plt.subplots()
    bars = ['Taxable Income', 'Tax Paid', 'Take Home', 'Total deductions']
    values = [taxable_income, tax, take_home, total_decuction]
    colors = ['red', 'black', 'blue', 'green']
    ax.bar(bars, values, color=colors)
    ax.set_ylabel("Amount (₹)")
    ax.set_title("Income Distribution")
    for i, v in enumerate(values):
        ax.text(i, v + income * 0.02, f"₹{v:,.0f}", ha='center', fontweight='bold')
    st.pyplot(fig)
 

#slider widget
st.markdown('-----')
st.write('#### Adjust the slidebar for the simple tax (0-100%)')
st.write(' Note: It is independent doesnt come under old or new regime')
perct = st.slider(f'Payable Tax for ₹ {income:,.2f} is: ', max_value=0, value=100)
st.write(f'{perct} %  tax -  ₹ {income * (perct/100):,.2f} need to pay')



#Old regiem table
st.markdown('-----')
col1,col2 = st.columns(2)

with col1:
    st.write('Checkout the Old Tax regiem below table: {Standard deduction is 25,000 }')
    st.markdown("<br>", unsafe_allow_html=True)  
    old = st.write(pd.DataFrame({
    'Tax Slab (₹)': ['1 to 2,50,000', '2,50,001 to 5,00,000','5,00,001 to 10,00,000', 'above 10,00,000'],
    'Tax Rate (%)': ['0',5,20,30],'Slab Value:':['2,50,000','2,50,000','5,00,000', '3,79,000']
    }))

#New regiem table
with col2:
    st.write('Checkout the New Tax regiem below table: {Standard decuction **75,000**}')
    # st.write('Standard dedcuction **75,000**')
    new = st.write(pd.DataFrame({
    'Tax Slab (₹)': ['1 to 4,00,000', '4,00,001 to 8,00,000','8,00,001 to 12,00,000','12,00,001 to 16,00,000','16,00,001 to 20,00,000','20,00,001 to 24,00,000', 'above 24,00,001'],
    'Tax Rate (%)': ['0',5,10,15,20,25,30], 'Slab Value:':['4,00,000','4,00,000','4,00,000','4,00,000','4,00,000','4,00,000','1,00,000']
    }))


