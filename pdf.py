import PyPDF2


def read_file():
    with open('./pdf/dummy.pdf', 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        print(reader.numPages)
        print(reader.getPage(0))


def rotate_file():
    with open('./pdf/dummy.pdf', 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)

        page = reader.getPage(0)

        page.rotateCounterClockwise(90)

        writer = PyPDF2.PdfFileWriter()
        writer.addPage(page)

        with open('test.pdf', 'wb') as fw:
            writer.write(fw)


if __name__ == '__main__':
    read_file()
    rotate_file()
