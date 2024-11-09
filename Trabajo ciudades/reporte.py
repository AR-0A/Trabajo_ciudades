
#En este módulo se generará el informe en PDF

from fpdf import FPDF

def generar_reporte(camino, distancia, archivo="reporte.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Reporte de Optimización de Rutas", ln=True, align="C")
    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 10, f"Ruta más corta encontrada: {' -> '.join(camino)}", ln=True)
    pdf.cell(0, 10, f"Distancia total: {distancia:.2f} km", ln=True)
    pdf.output(archivo)
