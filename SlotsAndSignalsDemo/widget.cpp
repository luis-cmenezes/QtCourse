#include "widget.h"
#include "ui_widget.h"

Widget::Widget(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::Widget)
{
    ui->setupUi(this);

    //String notation
    /*
    connect(ui->horizontalSlider,SIGNAL(valueChanged(int)),
            ui->progressBar,SLOT(setValue(int)));*/

    //Functor notation
    /*connect(ui->horizontalSlider,&QSlider::valueChanged,
            ui->progressBar,&QProgressBar::setValue);*/

    //Lambda notation
    connect(ui->horizontalSlider,&QSlider::valueChanged,
    [=]()
    {
        ui->progressBar->setValue(ui->horizontalSlider->value());
    });

    connect(ui->horizontalSlider,&QSlider::valueChanged,
    [=]()
    {
        if(ui->horizontalSlider->value() == 100)
        {
            ui->label->setText("Congratulations, you've completed.");
        }else
            ui->label->setText("");
    });

}

Widget::~Widget()
{
    delete ui;
}

