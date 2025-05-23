from extractor import MemorialPDFExtractor
from builder import VerticeTableBuilder
from exporters import ExporterFactory

def main():
    caminho_pdf = "exemplos-entrada/MEMORIAL SIGEF GLEBA 01 - 222,7794ha.pdf"
    formato_saida = "word"  # opcoes: "excel/word"
    caminho_saida = f"exemplos-saida/memorial_sigef.{ 'xlsx' if formato_saida == 'excel' else 'docx'}"

    extractor = MemorialPDFExtractor(caminho_pdf)
    registros = extractor.extract()

    tabela = VerticeTableBuilder(registros).build_dataframe()
    exporter = ExporterFactory.get_exporter(formato_saida)
    exporter.export(tabela, caminho_saida)


if __name__ == "__main__":
    main()
