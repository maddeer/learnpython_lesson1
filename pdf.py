from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        # Logo
        #self.image('logo_pb.png', 10, 8, 33)
        # Arial bold 15
        self.set_font('Arial', 'B', 10)
        # Move to the right
        self.cell(0, 10, book_name, 'B')
        # Title
        self.cell(0, 10, title, 'T', 0, 'R')
        # Line break
        self.ln(10)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, str(self.page_no()) + '/{nb}', 0, 0, 'R')

    def chapter_title(self, num, label):
        # Arial 12
        self.set_font('Arial', '', 12)
        # Background color
        #self.set_fill_color(200, 220, 255)
        # Title
        self.cell(0, 6, 'Chapter %d : %s' % (num, label), 0, 1, 'L', 0)
        # Line break
        self.ln(4)

    def chapter_body(self, name):
        # Read text file
        txt = name
        # Times 12
        self.set_font('Times', '', 12)
        # Output justified text
        self.multi_cell(0, 5, txt)
        # Line break
        self.ln()
        # Mention in italics
        self.set_font('', 'I')
        self.cell(0, 5, '(end of excerpt)')

    def print_chapter(self, num, title, name):
        self.add_page()
        self.chapter_title(num, title)
        self.chapter_body(name)

# Instantiation of inherited class

if __name__ == '__main__':
    pdf = PDF()
    pdf.alias_nb_pages()
    book_name = 'COOL BOOK: VERSION TOO MACH'
    title = 'My long Title'
    pdf.add_page()
    pdf.set_font('Times', '', 12)
    for i in range(1, 41):
        big_string = 'Printing line number asdfasdfasdfadfasfasfa asdfasf asdfasdfa asdfasfasf asdfasfasf asdfasfasf asfasf asfasf    asf asdfasdf asdfasfagg regagvafwe4ta hthwer gasgvawef adfgasdfgawertargatesabgsrthwsr5tgh as asfasdfa asdf  ' + str(i) 
        pdf.multi_cell(0, 5, big_string, 0, 'L')
    title = 'My other long Title'
    pdf.add_page()
    for i in range(1, 41):
        pdf.cell(0, 10, 'Printing line number ' + str(i), 0, 1)

    pdf.set_title(title)
    pdf.set_author('Jules Verne')
    pdf.print_chapter(1, 'A RUNAWAY REEF', big_string)
    pdf.print_chapter(2, 'THE PROS AND CONS', big_string)
    pdf.output('tuto2.pdf', 'F')
