def C_visualizacion(df):
    import streamlit as st
    import pandas as pd
    import pickle
    import numpy as np
    import plotly.express as px
    import matplotlib.pyplot as plt
    import plotly.graph_objects as go
    import seaborn as sns
    from sklearn.preprocessing import MinMaxScaler
    from scipy import interpolate


    st.header("Visualización del Análisis Exploratorio de Datos (EDA)")
    # Agrega tu código para visualizaciones EDA aquí
    st.write("Aquí irán los gráficos y visualizaciones del EDA.")

    st.dataframe(df)

    df_count = df.groupby('Deserción').count().reset_index()
    fig = px.pie(df_count, values="ID Empleado", names="Deserción", title="Deserción")
    st.plotly_chart(fig)

    # Agrupar por 'Satisfacción del Trabajo'
    df_count5 = df.groupby('Satisfacción del Trabajo').count().reset_index()

    # Crear gráfico de pastel para 'Satisfacción del Trabajo'
    fig5 = px.pie(df_count5, values="ID Empleado", names="Satisfacción del Trabajo", title="Satisfacción del Trabajo")
    st.plotly_chart(fig5)

    df_pareto = df['Rol de Trabajo'].value_counts()
    pareto_cumulative = df_pareto.cumsum() / df_pareto.sum() * 100

    # Crear la figura
    fig1 = go.Figure()

    # Barras de frecuencia
    fig1.add_trace(go.Bar(
        x=df_pareto.index,
        y=df_pareto.values,
        name='Frecuencia',
        marker_color='blue',
        yaxis='y1'
    ))

    # Línea de porcentaje acumulado
    fig1.add_trace(go.Scatter(
        x=df_pareto.index,
        y=pareto_cumulative,
        name='Porcentaje Acumulado',
        mode='lines+markers',
        line=dict(color='orange', width=2),
        marker=dict(symbol='circle'),
        yaxis='y2'
    ))

    # Agregar línea del 80%
    fig1.add_shape(
        type="line",
        x0=-0.5,
        x1=len(df_pareto) - 0.5,
        y0=80,
        y1=80,
        line=dict(color='red', dash='dash'),
        xref="x",
        yref="y2"
    )

    # Configuración de los ejes y el diseño
    fig1.update_layout(
        title='Gráfico de Pareto',
        xaxis=dict(title='Categoría'),
        yaxis=dict(
            title='Frecuencia',
            showgrid=False,
            side='left'
        ),
        yaxis2=dict(
            title='Porcentaje Acumulado (%)',
            overlaying='y',
            side='right',
            showgrid=False
        ),
        legend=dict(x=0.5, y=-0.2, orientation='h'),
        template='plotly_white',
        height=600,
        width=900
    )

    st.plotly_chart(fig1)

    # Gráfico de violín para 'Distancia a Casa' vs 'Trabajo Remoto'
    fig_violin = px.violin(
        df,
        x='Trabajo Remoto',
        y='Distancia a Casa',
        box=True,
        points='all',
        color='Trabajo Remoto',
        title="Gráfico de Violín: Distancia a Casa vs Trabajo Remoto",
        color_discrete_sequence=['orange', 'purple']
    )
    st.plotly_chart(fig_violin, use_container_width=True, key="violin_plot")

    # Variables a graficar
    hist_columns = ['Edad', 'Antigüedad en la Empresa', 'Ingreso Mensual']

    for col in hist_columns:
        # Crear histograma con un número específico de bins (por ejemplo 15)
        hist_values, bin_edges = np.histogram(df[col], bins=15)  # Cambia el número de bins aquí
        bin_centers = 0.5 * (bin_edges[:-1] + bin_edges[1:])
        
        # Crear figura
        fig_hist = go.Figure()
        
        # Barras del histograma
        fig_hist.add_trace(go.Bar(
            x=bin_centers,
            y=hist_values,
            name="Frecuencia",
            marker_color='blue',
            width=(bin_edges[1] - bin_edges[0]) * 0.8  # Controla el ancho de las barras
        ))

        # Interpolación suave para el contorno de las barras (SPLINE)
        tck = interpolate.splrep(bin_centers, hist_values, s=0)  # Ajuste spline sin suavizado
        spline_values = interpolate.splev(bin_centers, tck)  # Evalúa el spline
        
        # Curva de contorno con SPLINE
        fig_hist.add_trace(go.Scatter(
            x=bin_centers,
            y=spline_values,
            mode='lines',
            name='Contorno de barras',
            line=dict(color='red', width=2)
        ))
        
        # Configurar diseño
        fig_hist.update_layout(
            title=f"Histograma de {col} con Contorno de Barras",
            xaxis=dict(title=col),
            yaxis=dict(title="Frecuencia"),
            bargap=0.2,  # Controla la separación entre barras
            template="plotly_white"
        )
        
        # Mostrar gráfico en Streamlit
        st.plotly_chart(fig_hist, use_container_width=True, key=f"hist_{col}")
