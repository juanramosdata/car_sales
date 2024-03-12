# Base de Datos - Car Sales

Se analizó un conjunto de datos correspondientes a la venta de vehículos. En la carpeta `notebooks` se encuentra el cuaderno de Jupyter Notebooks con el preprocesamiento de los datos.

Una vez los datos se procesaron, se guardaron en un nuevo archivo `processed.csv` que es el que definitivamente se importó en la aplicación de streamlit. Se desarrolló una página interactiva que entregara un informe claro para la gerencia de la empresa, donde se puede filtrar fácilmente la información mediante una barra lateral. El año de fabricación se modificó de la base de datos original, completándola con el promedio del año de fabricación de otros vehículos del mismo modelo. La columna `is_4wd` también se modificó para completarle los valores nulos y convertirla en una columna booleana. 

Dentro de la aplicación, en la parte izquierda se encuentra la barra lateral con los filtros que el director desee para su análisis. Por defecto, la página abre con todos los valores predeterminados, pero son fácilmente modificables con los métodos `multiselect` y `slider` de streamlit. Si los filtros no generan datos, se enviará un aviso de precaución y se pedirá que se modifiquen los filtros. Si los datos están filtrados correctamente, la página mostrará un resumen ejecutivo en la parte superior y tres gráficas en la parte inferior.

*Leer los datos:* 

Se mostrará el valor total de las ventas de vehículos en dólares de la información filtrada, luego mostrará el porcentaje de venta respecto al dataset completo e incluso lo mostrará en emojis y finalmente la cantidad de vehículos vendidos en ese filtro.

En la parte inferior mostrará tres gráficas interactivas de Plotly: las ventas totales filtradas por marca de vehículo y tipo de vehículo, organizada en orden descendente; la cantidad de vehículos vendidos organizados por marcas y tipo también; y, el total de ventas en dólares diario.

*Acceder a la aplicación:*

Debido a que la aplicación de Streamlit está desplegada a través de Render, se puede hacer fácilmente siguiendo el siguiente link: https://cars-sales-report.onrender.com/
