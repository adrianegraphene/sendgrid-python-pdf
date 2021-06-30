import pdfrw


def update_pdf(filename, personal_link):
    pdf = pdfrw.PdfReader(filename)  # Load the pdf
    new_pdf = pdfrw.PdfWriter()  # Create an empty pdf

    page_count = 0
    for page in pdf.pages:  # Go through the pages

        link = 0  # Links are in Annots, but some pages don't have links so Annots returns None
        for annot in page.Annots or []:
            print("Page=%s. Link=%s" % (page_count, link))
            old_url = annot.A.URI
            print(old_url)
            if page_count == 15 and link != 0:
                print("Changing link %s on last slide to %s" % (link, personal_link))
                modified_link = "(" + personal_link + ")"  # Note the brackets around the URL here
                new_url = pdfrw.objects.pdfstring.PdfString(modified_link)
                annot.A.URI = new_url  # Override the URL with ours

            link = link + 1

        new_pdf.addpage(page)
        page_count = page_count + 1

    new_pdf.write("FynCom-Pitch-Deck.pdf")
