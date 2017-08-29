import sys,os
from urllib import urlopen
from urllib import urlretrieve
from urllib2 import URLError, HTTPError
import argparse

base_url="https://arxiv.org/list/cs.AI/recent"
down_load_base_url="https://arxiv.org/pdf/"

def Get_Id(html_lines):
    html_lines.search("list-identifier")
    ID = html_lines.remove("><a href=")

def Get_WeekDayMonthYear(html_lines):
    html_lines.search("<h3>")
    Week, Day, Month, Year = html_line.sprip("," " ")

    return Week, Day, Month, Year

def Get_Title_and_Subject(html_lines):
    html_lines.search("Title::</span> ")
    Title = html_line
    html_lines.search("Subjects:</span>")
    Subject = html_line.rstrip("</span>",";")

    return Title, Subject

def Get_Authors(html_lines):
    html_lines.search("Authors:</span>")
    html_lines.next_line
    Authors = {}
    while (html_lines.search("<a>")):
        Authors.append(html_lines)
        Authors.remove("<a>")

        return Authors

def Get_Abstract(html_lines):
    html_lines.search("Abstract:</span>")
    Abstruct = ""
    while (~html_lines.search("</blockquote>"):
           Abstract = html_lines.append

    return Abstrsact

def Get_pdf(html_lines):
    html_lines.search("Download PDF")
    pdf_file = GetFile(base_url+"/"+id+".pdf")

    return pdf_file

def main():
    # arguments
    paser = argparse.ArgumentParser()
    paser.add_argument(--pdf_dir,   type=str, default='pdf_pod')
    paser.add_argument(--inf_dir,   type=str, default='inf_pod')
    paser.add_ardgment(--log_dir,   type=str, default='log_pod')
    paser.add_ardgment(--dat_dir,   type=str, default='dat_pod')
    args=argparse.ArgumentParser()

    # Open Log File
    log_file = open(argparse.log_dir, 'w')
    write(log_file, "{}: {} opened.".format(time, argparse.log_dir))

    # Open pdf Folder
    pdf_dir = open(argparse.pdf_dir, 'w')
    write(log_file, "{}: {} opened.".format(time, argparse.pdf_dir))

    # Open Title, Jubject, Authors, and File Name Folder
    inf_dir = open(argparse.inf_dir, 'w')
    write(log_file, "{}: {} opened.".format(time, argparse.inf_dir))

    # Open Database Folder
    dat_file = open(argparse.dat_dir, 'w')
    write(log_file, "{}: {} opened.".format(time, argparse.dat_dir))

    # Try accesing to Base Home page
    write(log_file, "{}: {} try.to access".format(time, base_url))
    html_lines = Access.to(base_url)

    tmp_day=1
    day=1

    counter=0

    year_counter=''
    month_counter=''
    week_counter=''
    day_counter=1

    Boot_Time = Get_TodayTime()
    while (Get_time() == Boot_Time):

        if counter != 1:
            # make today's dir
            mkdir(pdf_dir, "{}{}{}".format(Year, Month, Day))

            # make today's dir
            mkdir(inf_dir, "{}{}{}".format(Year, Month, Day))

        counter=1
        
        while html_lines != EOF:
            # Get ID
            ID = Get_Id(html_lines)
            time = Get_Time()
            write(log_file, "{}: {} got ID".format(time, ID))

            # Get pdf file
            pdf_file = Get_pdf(html_lines)
            time = Get_Time()
            write(log_file, "{}: got {}/{}.pdf file".format(time, base_url, id))

            # Get Time Stamp
            Week, Day, Month, Year = Get_WeekDayMonthYear(html_lines)
            time = Get_Time()
            write(log_file, "{}: {},{},{},{}".format(time, Week, Day, Month, Year))

            # Get Title and Subject
            Title, Jubject = Get_Title_and_Subject(html_lines)
            time = Get_Time()
            write(log_file, "{}: {},{}".format(time, Title, Jubject)

            # Get Authors
            Authors = Get_Authors(html_lines)
            time = Get_Time()
            write(log_file, "{}: {}".format(time, Authors)

            # Try accesing to Abstract page
            time = Get_Time()
            write(log_file, "{}: {} try to access".format(time, down_load_base_url+ID+'.pdf'))
            html_lines = Access.to(down_load_base_url+ID+'.pdf')
            Abstruct = txtGet_Abstract(html_lines)

            # pdf file store
            write(pdf_dir, pdf_file)

            # write pdf's infomation to inf_dir
            write(inf_dir, "[{}] {}, {}\n    {}\n    {}.pdf\n\n".format(counter, Get_Authors, Title, Get_Title_and_Subject, Abstruct, ID))

            #Update counter
            counter += 1

        
        # Update Sleep Timer
        tmp_day = day
        day, time = Get_TodayTime()
        if (day != tmp_day):
            Update_Time(Boot_Time)

#EOF