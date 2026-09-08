from pathlib import Path

from pdfminer.high_level import extract_text
from rapidocr import RapidOCR

HERE = Path(__file__).resolve().parent
MY_DOCUMENTS = HERE.parent.parent / "data" / "my_documents"

def pdfminer_example() -> str:
    # extract_text returns a single string
    text = extract_text(str(MY_DOCUMENTS / "Rivendell_Event_Email_Meeting_Minutes.pdf"))
    return text[:500]


def rapidocr_example() -> str:
    # returns an object with .texts as list[str]
    result = RapidOCR(params={"Global.log_level": "error"})(
        str(MY_DOCUMENTS / "Fondue_Recipe.png")
    )
    return "\n".join(result.txts or [])[:500]


if __name__ == "__main__":
    print(pdfminer_example())
    print(rapidocr_example())
