# Import python packages
import streamlit as st
import pandas as pd
from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col


# Write directly to the app
st.title("Zena's Amazing Athleisure Catalog")


# Get the current credentials
# session = get_active_session()

cnx = st.connection("snowflake")
session = cnx.session()

my_dataframe = session.table("ZENAS_ATHLEISURE_DB.PRODUCTS.catalog_for_website").select(col('Color_or_Style'),
                                                                                       col('price'),
                                                                                       col('direct_url'),
                                                                                       col('size_list'),
                                                                                       col('upsell_product_desc'))
pd_df = my_dataframe.to_pandas()
# st.dataframe(pd_df)

col_picker = st.selectbox(
    "Pick a sweatsuit color or style", pd_df['COLOR_OR_STYLE'] 
     )

# st.dataframe(data=my_dataframe, use_container_width=True)


if col_picker:
    st.image(pd_df.loc[pd_df['COLOR_OR_STYLE'] == col_picker, 'DIRECT_URL'].iloc[0], caption="Our warm, comfortable " + col_picker +
            " sweatsuit!")
    
    st.write('Price: ',  pd_df.loc[pd_df['COLOR_OR_STYLE'] == col_picker, 'PRICE'].iloc[0])
    
    st.write('Sizes Available: ',pd_df.loc[pd_df['COLOR_OR_STYLE'] == col_picker, 'SIZE_LIST'].iloc[0])

    st.write(pd_df.loc[pd_df['COLOR_OR_STYLE'] == col_picker, 'UPSELL_PRODUCT_DESC'].iloc[0])
