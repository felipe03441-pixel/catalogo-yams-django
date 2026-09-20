import pandas as pd

archivo_entrada = 'inventario_original.xlsm'
archivo_salida = 'inventario_catalogo.xlsx'

try:
    print(f"Cargando la hoja 'INVENTARIO' del archivo: {archivo_entrada}...")
    
    # Leemos el Excel sin asumir que la primera fila es el encabezado
    df = pd.read_excel(archivo_entrada, engine='openpyxl', sheet_name='INVENTARIO', header=None)
    
    # Buscamos automáticamente en qué fila están los títulos (buscando la palabra 'DESCRIPCION')
    fila_encabezado = df[df.apply(lambda x: x.astype(str).str.contains('DESCRIPCION', case=False, na=False).any(), axis=1)].index
    
    if fila_encabezado.empty:
        print("\nError: No se encontró la palabra 'DESCRIPCION' en ninguna celda de la hoja.")
    else:
        # Tomamos el número de la fila donde encontró los títulos
        indice_encabezado = fila_encabezado[0]
        print(f"¡Encabezados encontrados en la fila {indice_encabezado + 1} de Excel!")
        
        # Asignamos esa fila como los nombres reales de las columnas
        df.columns = df.iloc[indice_encabezado]
        
        # Nos quedamos solo con los datos de los productos (descartando los títulos y lo que haya arriba)
        df = df.iloc[indice_encabezado + 1:].reset_index(drop=True)
        
        # Limpiamos los nombres de las columnas por si tienen espacios en blanco invisibles
        df.columns = df.columns.astype(str).str.strip()
        
        # Seleccionamos las columnas que necesitamos
        columnas_utiles = ['DESCRIPCION', 'STOCK ACTUAL', 'COSTO UNITARIO']
        
        # Verificamos que ahora sí existan
        if not all(col in df.columns for col in columnas_utiles):
             print("\nError: Faltan columnas. Columnas detectadas ahora:")
             print(df.columns.tolist())
        else:
            df_limpio = df[columnas_utiles].copy()
            
            # Limpieza de datos
            df_limpio = df_limpio.dropna(subset=['DESCRIPCION'])
            df_limpio['STOCK ACTUAL'] = pd.to_numeric(df_limpio['STOCK ACTUAL'], errors='coerce')
            df_limpio = df_limpio[df_limpio['STOCK ACTUAL'] > 0]
            
            # Renombramos para Django
            df_limpio = df_limpio.rename(columns={
                'DESCRIPCION': 'nombre',
                'COSTO UNITARIO': 'precio',
                'STOCK ACTUAL': 'stock'
            })
            
            # Guardamos el resultado final
            df_limpio.to_excel(archivo_salida, index=False)
            print(f"\n¡Éxito! El archivo limpio se guardó como: {archivo_salida}")
            print("\n--- Vista previa de los productos listos ---")
            print(df_limpio.head())

except FileNotFoundError:
    print(f"Error: No se encontró '{archivo_entrada}'.")
except Exception as e:
    print(f"Ocurrió un error inesperado al leer el archivo: {e}")