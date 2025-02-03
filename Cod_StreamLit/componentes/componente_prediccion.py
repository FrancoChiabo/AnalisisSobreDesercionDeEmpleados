def C_prediccion(model2):
    
    import streamlit as st
    import pandas as pd
    import numpy as np
    from sklearn.preprocessing import MinMaxScaler

    st.header("Modelo de Predicción del Ingreso Mensual")

    # Descripción
    st.write("Predicción con Modelo Bosque Aleatório, ingrese los valores de las características para obtener el Ingreso Mensual.")

    import streamlit as st

    # Opciones para cada selectbox (definidos previamente)
    gender_options1 = {
        "Masculino": 0,
        "Femenino": 1,
    }

    role_options1 = {
        'Media': 0, 'Educación': 1, 'Tecnología': 2, 'Finanzas': 3, 
        'Cuidado de la salud': 4, 'Ejecutiva/o de ventas': 5, 'Gerente': 6, 'Director de Investigación': 7,
        'Representante de ventas': 8, 'Técnica/o de laboratorio': 9, 'Científica/o de investigación': 10,
        'Director de Manufactura': 11, 'Representante de atención médica': 12, 'Recursos humanos': 13
    }

    balance_options1 = {
        'Pobre': 0, 'Justo': 1, 'Bueno': 2, 'Excelente': 3
    }

    satisfaccion_options1 = {
        'Bajo': 0, 'Medio': 1, 'Alto': 2, 'Muy Alto': 3
    }

    desempeno_options1 = {
        'Bajo': 0, 'Por debajo del promedio': 1, 'Promedio': 2, 'Alto': 3
    }

    overtime_options1 = {
        'Si': 1, 'No': 0
    }

    educacion_options1 = {
        'Secundario': 0, 
        'Grado asociado': 1, 
        'Licenciatura': 2, 
        'Maestría': 3, 
        'Doctor en Filosofía': 4
    }

    civil_options1 = {
        'Divorciado': 0, 'Casado': 1, 'Soltero': 2
    }

    job_options1 = {
        'Mid': 0, 'Entry': 1, 'Senior': 2
    }

    tamano_options1 = {
        'Media': 0, 'Pequeña': 1, 'Grande': 2
    }

    remoto_options1 = {
        'Si': 1, 'No': 0
    }

    liderazgo_options1 = {
        'Si': 1, 'No': 0
    }

    innovacion_options1 = {
        'Si': 1, 'No': 0
    }

    reputacion_options1 = {
        'Justa': 0, 'Buena': 1, 'Excelente': 2, 'Pobre': 3
    }

    reconocimiento_options1 = {
        'Bajo': 0, 'Medio': 1, 'Alto': 2, 'Muy Alto': 3
    }

    desercion_options1 = {
        'Permanece': 0, 'Deserción': 1
    }

    # Creando 4 columnas
    col1, col2, col3, col4 = st.columns(4)

    # En la primera columna
    with col1:
        gender_label1 = st.selectbox("Seleccione el Género", options=list(gender_options1.keys()), key='gender2')
        role_label1 = st.selectbox("Seleccione el Rol de Trabajo", options=list(role_options1.keys()), key='role2')
        balance_label1 = st.selectbox("Seleccione el Balance Trabajo-Vida", options=list(balance_options1.keys()), key='balance2')
        satisfaccion_label1 = st.selectbox("Seleccione la Satisfacción del Tabajo", options=list(satisfaccion_options1.keys()), key='satisfaccion2')
        desempeno_label1 = st.selectbox("Seleccione el Desempeño", options=list(desempeno_options1.keys()), key='desempeno2')
        overtime_label1 = st.selectbox("Seleccione si tiene Horas Extras", options=list(overtime_options1.keys()), key='overtime2')
        educacion_label1 = st.selectbox("Seleccione el Nivel de Educación", options=list(educacion_options1.keys()), key='educacion2')
        civil_label1 = st.selectbox("Seleccione el Estado Civil", options=list(civil_options1.keys()), key='civil2')

    # En la segunda columna
    with col2:
        job_label1 = st.selectbox("Seleccione el Nivel de Trabajo", options=list(job_options1.keys()), key='job2')
        tamano_label1 = st.selectbox("Seleccione el Tamaño de Empresa", options=list(tamano_options1.keys()), key='tamano2')
        remoto_label1 = st.selectbox("Seleccione si hace Trabajo Remoto", options=list(remoto_options1.keys()), key='remoto')
        liderazgo_label1 = st.selectbox("Seleccione si tiene Oportunidades de Liderazgo", options=list(liderazgo_options1.keys()), key='liderazgo2')
        innovacion_label1 = st.selectbox("Seleccione si tiene Oportunidades de Innovación", options=list(innovacion_options1.keys()), key='innovacion2')
        reputacion_label1 = st.selectbox("Seleccione la Reputación de la Empresa", options=list(reputacion_options1.keys()), key='reputacion2')
        reconocimiento_label1 = st.selectbox("Seleccione el Reconocimiento a Empleado", options=list(reconocimiento_options1.keys()), key='reconocimiento2')
        desercion_label1 = st.selectbox("Seleccione estado de Deserción", options=list(desercion_options1.keys()), key='desercion2')



    with col3:
        # Crear un formulario para la entrada de datos del usuario
        input1_data = {}

        input1_data['Edad+norm'] = st.number_input("Ingrese el valor de Edad", min_value=18, max_value=60, value=18, key='numero11')
        input1_data['Género+norm'] = gender_options1[gender_label1]
        input1_data['Antigüedad en la Empresa+norm'] = st.number_input("Ingrese el valor de Antigüedad en la Empresa", min_value=0, max_value=43, value=0, key='numero12')
        input1_data['Rol de Trabajo+norm'] = role_options1[role_label1]
        input1_data['Balance Trabajo-Vida+norm'] = balance_options1[balance_label1]
        input1_data['Satisfacción del Trabajo+norm'] = satisfaccion_options1[satisfaccion_label1]
        input1_data['Desempeño+norm'] = desempeno_options1[desempeno_label1]
        input1_data['Número de Promociones+norm'] = st.number_input("Ingrese el valor de Número de Promociones", min_value=0, max_value=4, value=0, key='numero13')
        input1_data['Horas Extras+norm'] = overtime_options1[overtime_label1]
        input1_data['Distancia a Casa+norm'] = st.number_input("Ingrese el valor de Distancia a Casa", min_value=1, max_value=99, value=1, key='numero14')
        input1_data['Nivel de Educación+norm'] = educacion_options1[educacion_label1]
        input1_data['Estado Civil+norm'] = civil_options1[civil_label1]
        input1_data['Número de Dependientes+norm'] = st.number_input("Ingrese el valor de Número de Dependientes", min_value=0, max_value=6, value=0, key='numero15')
        input1_data['Nivel de Trabajo+norm'] = job_options1[job_label1]
        input1_data['Tamaño de Empresa+norm'] = tamano_options1[tamano_label1]
        input1_data['Meses desde el último evento+norm'] = st.number_input("Ingrese el valor de Meses desde el último evento", min_value=2, max_value=180, value=2, key='numero16')
        input1_data['Trabajo Remoto+norm'] = remoto_options1[remoto_label1]
        input1_data['Oportunidades de Liderazgo+norm'] = liderazgo_options1[liderazgo_label1]
        input1_data['Oportunidades de Innovación+norm'] = innovacion_options1[innovacion_label1]
        input1_data['Reputación de la Empresa+norm'] = reputacion_options1[reputacion_label1]
        input1_data['Reconocimiento a Empleado+norm'] = reconocimiento_options1[reconocimiento_label1]
        input1_data['Deserción+norm'] = desercion_options1[desercion_label1]

    with col4:
        # Crear botón para realizar predicción
        if st.button("Realizar Predicción"):
            # Convertir los datos en un array o DataFrame de acuerdo al modelo
            input1_df = pd.DataFrame([input1_data])
            # Realizar la predicción
            prediction_normalized1 = model2.predict(input1_df)

            # Desnormalizar la salida, si es necesario (por ejemplo, si predice un salario)
            min_val, max_val = 1009, 19999 # Rango original usado en la normalización del entrenamiento
            prediction_original1 = prediction_normalized1 * (max_val - min_val) + min_val

            # Mostrar el resultado
            st.markdown(f"<h2 style='color: #4CAF50; text-align: center;'>La predicción del Ingreso Mensual es:</h2>", unsafe_allow_html=True)
            st.markdown(f"<h3 style='color: #4CAF50; text-align: center;'>${prediction_original1[0]}</h3>", unsafe_allow_html=True)
