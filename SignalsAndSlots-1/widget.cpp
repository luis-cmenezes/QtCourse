#include "widget.h"
#include "ui_widget.h"
#include <QDebug>

Widget::Widget(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::Widget)
{
    ui->setupUi(this);

    //String notation
    connect(ui->pushButton,SIGNAL(clicked()),
            this,SLOT(changeTextStringNotation()));

    //Lamba notation
    connect(ui->pushButton,&QPushButton::clicked,
    [=]()
    {
        qDebug() << "User clicked on button.";
        ui->label->setText("Lambda");
    });

    //Functor notation
    connect(ui->pushButton,&QPushButton::clicked,this,&Widget::changeTextFunctorNotation);
}

Widget::~Widget()
{
    delete ui;
}

void Widget::changeTextStringNotation()
{
    qDebug() << "User clicked on button.";
    ui->label->setText("Hello there");
}

void Widget::changeTextFunctorNotation()
{
    qDebug() << "User clicked on button.";
    ui->label->setText("Hello there");
}
