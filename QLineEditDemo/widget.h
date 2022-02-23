#ifndef WIDGET_H
#define WIDGET_H

#include <QWidget>
#include <QPushButton>
#include <QLabel>
#include <QLineEdit>
#include <QDebug>
#include <QMessageBox>

class Widget : public QWidget
{
    Q_OBJECT

public:
    Widget(QWidget *parent = nullptr);
    ~Widget();

private:
    QLabel *firstNameLabel = new QLabel("First Name", this);
    QLineEdit *firstNameLineEdit = new QLineEdit(this);

    QLabel *lastNameLabel = new QLabel("Last Name", this);
    QLineEdit *lastNameLineEdit = new QLineEdit(this);

    QLabel *cityLabel = new QLabel("City", this);
    QLineEdit *cityLineEdit = new QLineEdit(this);

    QPushButton *grabDataButton = new QPushButton("Grab data", this);

};
#endif // WIDGET_H
