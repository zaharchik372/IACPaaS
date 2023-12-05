import sys, os
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, \
    QMessageBox, QDialog
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class CosmeticsSelectorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.spisok_result_tovar = []
        self.setWindowTitle("Подбор косметики")
        self.setGeometry(100, 100, 800, 500)

        self.init_ui()

    def init_ui(self):
        layout = self.create_layout()
        self.setLayout(layout)

    def create_layout(self):

        main_layout = QVBoxLayout()


        def combo_box_1_changed():
            selected_text = combo_box_1.currentText()
            combo_box_2.clear()
            if selected_text == "Сухость кожи":
                combo_box_2.addItems([
                    "На коже есть шелушения",
                    "Шелушения отсутствуют, кожа достаточно увлажнена"])
            elif selected_text == "Ощущения после умывания":
                combo_box_2.addItems([
                    "Чувство стянутости",
                    "Появляется жирный блеск",
                    "Дискомфорт отсутствует"])
            elif selected_text == "Жирный блеск":
                combo_box_2.addItems([
                    "Жирный блеск отсутствует",
                    "Слабый, в области Т-зоны (лоб, нос, подбородок)",
                    "Заметный блеск на всём лице"])
            elif selected_text == "Поры":
                combo_box_2.addItems([
                    "Узкие, незаметные",
                    "Расширенные"])
            elif selected_text == "Чувствительность":
                combo_box_2.addItems([
                    "Аллергические реакции",
                    "Кожа реагирует на холодный воздух, сухой воздух"])
            elif selected_text == "Тон кожи":
                combo_box_2.addItems([
                    "Серый, тусклый",
                    "Здоровый, однородный"])
            elif selected_text == "Морщины":
                combo_box_2.addItems([
                    "Возрастные",
                    "Отсутствуют"])

        label_2 = QLabel("Выберите характеристику: ")
        combo_box_2 = QComboBox()
        combo_box_2.addItems([
            "На коже есть шелушения",
            "Шелушения отсутствуют, кожа достаточно увлажнена"])

        QLabel("Выберите оценку состояния кожи:")
        combo_box_1 = QComboBox()
        combo_box_1.addItems(["Сухость кожи",
                              "Ощущения после умывания",
                              "Жирный блеск",
                              "Поры",
                              "Чувствительность",
                              "Тон кожи",
                              "Морщины"])
        combo_box_1.currentIndexChanged.connect(combo_box_1_changed)


        QLabel("Выберите название типа кожи: ")
        combo_box_3 = QComboBox()
        combo_box_3.addItems([
            "Сухая",
            "Жирная",
            "Нормальная",
            "Чувствительная"])

        QLabel("Выберите этап ухода: ")
        combo_box_4 = QComboBox()
        combo_box_4.addItems([
            "Очищение",
            "Тонизация",
            "Увлажнение",
            "Дополнительный уход"])

        QLabel("Выберите тип уходовой продукции: ")
        combo_box_5 = QComboBox()
        combo_box_5.addItems([
            "Крем",
            "Сыворотка",
            "Лосьон",
            "Тоник",
            "Маска",
            "Скраб",
            "Мицеллярная вода",
            "Эмульсия",
            "Гель для умывания"])

        QLabel("Выберите цель ухода: ")
        combo_box_6 = QComboBox()
        combo_box_6.addItems(["Основной уход", "Антивозрастной уход"])
        combo_box_1.setStyleSheet(
            "font-family: Times New Roman; font-size: 16px; background-color: "
            "#F2F2F2; color: #333; border: 1px solid #888;")
        combo_box_2.setStyleSheet(
            "font-family: Times New Roman; font-size: 16px; background-color: "
            "#F2F2F2; color: #333; border: 1px solid #888;")
        combo_box_3.setStyleSheet(
            "font-family: Times New Roman; font-size: 16px; background-color: "
            "#F2F2F2; color: #333; border: 1px solid #888;")
        combo_box_4.setStyleSheet(
            "font-family: Times New Roman; font-size: 16px; background-color: "
            "#F2F2F2; color: #333; border: 1px solid #888;")
        combo_box_5.setStyleSheet(
            "font-family: Times New Roman; font-size: 16px; background-color: "
            "#F2F2F2; color: #333; border: 1px solid #888;")
        combo_box_6.setStyleSheet(
            "font-family: Times New Roman; font-size: 16px; background-color: "
            "#F2F2F2; color: #333; border: 1px solid #888;")
        label_1 = QLabel(
            "<span style='font-family: Arial; font-size: 16px; color: #333;'>Выберите оценку состояния кожи:</span>")
        label_2 = QLabel(
            "<span style='font-family: Arial; font-size: 16px; color: #333;'>Выберите характеристику:</span>")
        label_3 = QLabel(
            "<span style='font-family: Arial; font-size: 16px; color: #333;'>Выберите название типа кожи:</span>")
        label_4 = QLabel("<span style='font-family: Arial; font-size: 16px; color: #333;'>Выберите этап ухода:</span>")
        label_5 = QLabel(
            "<span style='font-family: Arial; font-size: 16px; color: #333;'>Выберите тип уходовой продукции:</span>")
        label_6 = QLabel("<span style='font-family: Arial; font-size: 16px; color: #333;'>Выберите цель ухода:</span>")



        def show_selected_text():

            cream = [
                "TOLERIANE SENSITIVE RICHE НАСЫЩЕННЫЙ КРЕМ Увлажняющий крем для сухой чувствительной кожи",
                "HYDRA PHASE HA НАСЫЩЕННЫЙ КРЕМ Интенсивный увлажняющий уход для обезвоженной кожи нормального и сухого типа",
                "TOLERIANE SENSITIVE ЛЕГКИЙ КРЕМ Увлажняющий крем для чувствительной кожи",
                "TOLERIANE DERMATOLOGY КРЕМ Интенсивный успокаивающий уход",
                "REDERMIC RETINOL Интенсивный концентрированный гель-крем для коррекции морщин и рельефа кожи",
                "Матирующий гель-крем 'Бархатный финиш'",
                "Себорегулирующий крем 'Чистый баланс'",
                "Увлажняющий крем 'Аква фреш'",
                "Легкий матирующий крем 'Гладкая текстура'",
                "Крем для контроля блеска 'Матовый контроль'",
                "Гель-крем 'Свежее ощущение'",
                "Интенсивный увлажняющий крем 'Экстра влажность'",
                "Питательный крем 'Восстановление кожи'",
                "Увлажняющий крем 'Нежное сияние'",
                "Богатый уход 'Максимальное питание'",
                "Крем для сухой кожи 'Увлажнение и уход'",
                "Успокаивающий крем 'Сохранение комфорта'",
                "Увлажняющий крем для чувствительной кожи 'Нежное обертывание'",
                "Специальный крем для склонной к аллергическим реакциям",
                "Успокаивающий крем 'Мягкое успокоение'",
                "Антивозрастной крем для чувствительной кожи",
                "Нежный уход для чувствительной кожи 'Тихая гармония'",
                "Крем для реактивной кожи 'Спокойное сияние'",
                "Легкий дневной крем 'Естественная гармония'",
                "Крем для поддержания сияния кожи 'Сияющая красота'",
                "Увлажняющий крем 'Восстановление равновесия'",
                "Антивозрастной крем 'Время красоты'",
                "Крем для ежедневного ухода 'Здоровая кожа'",
                "Уход за нормальной кожей 'Идеальное совершенство'"
            ]

            serum = [
                "TOLERIANE ULTRA DERMALLERGO Интенсивная успокаивающая сыворотка, активирующая защитную функцию кожи, "
                "для лица и области вокруг глаз",
                "HYALU B5 УХОД Увлажняющий уход против морщин",
                "RETINOL B3 СЫВОРОТКА Интенсивная сыворотка против глубоких морщин для выравнивания цвета "
                "лица и текстуры кожи",
                "Интенсивная сыворотка для увлажнения и осветления кожи",
                "Сыворотка с антивозрастным эффектом 'Молодость и сияние'",
                "Сыворотка для укрепления кожи 'Упругость и тонус'",
                "Сыворотка для борьбы с пигментацией 'Равномерный цвет лица'",
                "Сыворотка с антиоксидантами 'Защита от стресса кожи'",
                "Сыворотка с гиалуроновой кислотой 'Глубокое увлажнение'",
                "Антивозрастная сыворотка с коллагеном",
                "Сыворотка с экстрактом розы для освежения кожи",
                "Сыворотка с ретинолом для улучшения текстуры кожи",
                "Сыворотка для борьбы с покраснениями и воспалениями",
            ]

            lotion = ['EFFACLAR ЛОСЬОН Лосьон для кожи лица для сужения пор',
                      "EFFACLAR Очищающий лосьон для лица с экстрактом зеленого чая",
                      "EFFACLAR Увлажняющий лосьон для лица с гиалуроновой кислотой",
                      "Лосьон для сужения пор 'Чистая кожа'",
                      "Очищающий лосьон с экстрактом зеленого чая",
                      "Увлажняющий лосьон с гиалуроновой кислотой",
                      "Лосьон для ухода за чувствительной кожей 'Нежное успокоение'",
                      "Матирующий лосьон для контроля блеска",
                      "Тонизирующий лосьон с алое вера и ромашкой",
                      "Лосьон для интенсивного увлажнения и питания",
                      "Лосьон для нормализации секреции кожного сала",
                      "Лосьон для омоложения и укрепления кожи",
                      "Лосьон с антивозрастными компонентами 'Молодость и сияние'",
                      ]

            tonic = ["УСПОКАИВАЮЩИЙ ТОНИК Успокаивает, тонизирует и защищает кожу",
                     "HYALU Восстанавливающий тоник для лица с алое вера и ромашкой",
                     "EFFACLAR Матирующий тоник для лица с салициловой кислотой",
                     "Успокаивающий тоник 'Сохранение гармонии кожи'",
                     "Восстанавливающий тоник для лица 'Сияющая свежесть'",
                     "Матирующий тоник для сияющей кожи",
                     "Тоник для увлажнения 'Свежесть и увлажнение'",
                     "Тоник с антивозрастными компонентами 'Молодость и красота'",
                     "Увлажняющий тоник с морскими минералами",
                     "Тоник для борьбы с покраснениями и раздражениями",
                     "Тоник с экстрактом огурца для освежения кожи",
                     "Тоник с витаминами для сияющей и здоровой кожи",
                     "Тоник для укрепления сосудов и снятия отечности",
                     ]

            mask = ["EFFACLAR МАСКА Очищающая матирующая маска для жирной проблемной кожи",
                    "Маска с глиной и зеленым чаем для жирной кожи",
                    "Успокаивающая маска с огурцом и алоэ вера для чувствительной кожи",
                    "Омолаживающая маска с гиалуроновой кислотой для зрелой кожи",
                    "Маска с морскими минералами для увлажнения и омоложения кожи",
                    "Очищающая маска с глиной и активированным углем",
                    "Увлажняющая маска с гиалуроновой кислотой",
                    "Антивозрастная маска с коллагеном и пептидами",
                    "Маска с алое вера для ухода за чувствительной кожей",
                    "Маска с экстрактом зеленого чая для сужения пор",
                    "Маска с витамином C для осветления и равномерности тона",
                    "Успокаивающая маска с огурцом и алое вера",
                    "Маска с морскими минералами для увлажнения и омоложения",
                    "Маска с ретинолом для регенерации кожи",
                    "Омолаживающая маска с пептидами и антиоксидантами",
                    ]

            scrub = ["ФИЗИОЛОГИЧЕСКИЙ СКРАБ Ультрамягкий скраб для всех типов кожи",
                     "Освежающий гранулированный скраб 'Цитрусовое сияние'",
                     "Деликатный антиоксидантный скраб 'Золотой мед и овес'",
                     "Физиологический скраб 'Деликатное очищение'",
                     "Очищающий скраб с частицами апельсиновой корки",
                     "Скраб с морской солью для глубокого очищения",
                     "Скраб с рисовыми микро-частицами для сияющей кожи",
                     "Скраб с кофеином для подтяжки и стяжки кожи",
                     "Освежающий скраб с ментоловым эффектом",
                     "Деликатный антиоксидантный скраб 'Золотой мед и овес'",
                     "Ультрамягкий скраб для чувствительной кожи",
                     "Скраб с пептидами и экстрактом лаванды",
                     "Скраб с гранулами из ореха макадамии",
                     ]

            micellar_water = ["МИЦЕЛЛЯРНАЯ ВОДА EFFACLAR ULTRA Очищение для жирной проблемной кожи",
                              "МИЦЕЛЛЯРНАЯ ВОДА ULTRA SENSITIVE Очищение для чувствительной кожи лица и глаз",
                              "МИЦЕЛЛЯРНАЯ ВОДА ULTRA REACTIVE Очищение для склонной к аллергии чувствительной кожи",
                              "Мицеллярная вода для чувствительной кожи 'Нежное очищение'",
                              "Мицеллярная вода для снятия макияжа 'Эффективное удаление'",
                              "Очищающая мицеллярная вода для жирной кожи",
                              "Мицеллярная вода с экстрактом розы для освежения",
                              "Мицеллярная вода для ухода за нормальной кожей",
                              "Увлажняющая мицеллярная вода с гиалуроновой кислотой",
                              "Мицеллярная вода для снятия водостойкого макияжа",
                              "Мицеллярная вода для сияющей кожи с микрочастицами",
                              "Очищающая мицеллярная вода с алое вера",
                              "Мицеллярная вода для снятия макияжа глаз и губ",
                              ]

            emulsion = ["EFFACLAR K(+) Эмульсия для жирной кожи",
                        "Легкая восстанавливающая эмульсия 'Сияние розы'",
                        "Увлажняющая эмульсия 'Морской бриз'",
                        "Эмульсия для жирной кожи с антиоксидантами",
                        "Легкая восстанавливающая эмульсия 'Сияние розы'",
                        "Увлажняющая эмульсия 'Морской бриз'",
                        "Эмульсия с алое вера для чувствительной кожи",
                        "Матирующая эмульсия для контроля блеска",
                        "Эмульсия для нормализации кожного сала",
                        "Антивозрастная эмульсия с молекулами ретинола",
                        "Эмульсия для укрепления и увлажнения кожи",
                        "Эмульсия с витаминами для сияющей кожи",
                        "Легкая эмульсия с антивозрастными компонентами",
                        ]

            Washing_gel = ["EFFACLAR GEL Очищающий пенящийся гель для жирной кожи",
                           "TOLERIANE ОЧИЩАЮЩИЙ ГЕЛЬ-УХОД Очищающий гель-уход для умывания",
                           "Очищающий гель для жирной кожи с салициловой кислотой",
                           "Деликатный гель для умывания с экстрактом огурца",
                           "Увлажняющий гель для нормальной кожи с экстрактом алое вера",
                           "Гель для умывания с оливковым маслом для ухода за сухой кожей",
                           "Очищающий гель-уход с экстрактом ромашки для чувствительной кожи",
                           "Гель-уход с гранулами для глубокого очищения",
                           "Гель для умывания с молочной кислотой для омоложения",
                           "Очищающий гель с антивозрастными компонентами",
                           "Успокаивающий гель для ухода за раздраженной кожей",
                           "Мягкий гель для умывания для ежедневного использования",
                           ]
            pos = window.pos()
            x, y = pos.x(), pos.y()

            dialog = QDialog()
            dialog.setGeometry(x, y, 650, 200)

            dialog.setWindowTitle("Результат тестирования")
            self.spisok_result_tovar.clear()
            self.spisok_result_tovar.append(combo_box_1.currentText())
            self.spisok_result_tovar.append(combo_box_2.currentText())
            self.spisok_result_tovar.append(combo_box_3.currentText())
            self.spisok_result_tovar.append(combo_box_4.currentText())
            self.spisok_result_tovar.append(combo_box_5.currentText())
            self.spisok_result_tovar.append(combo_box_6.currentText())

            combo_box_1.currentText()
            label = QLabel(
                f"Исходя из предоставленных параметров и характеристик кожи, можно сделать следующие выводы по типу кожи: '{self.spisok_result_tovar[2].lower()}'\n"
                f"Ваше состояние проявляет: {self.spisok_result_tovar[0].lower()}, и выделяет: {self.spisok_result_tovar[1].lower()}.\n\n"
                f"Это свидетельствует о необходимом лечении, для Вас необходимо: {self.spisok_result_tovar[3].lower()}. \n"
                f"Данную процедуру Вы будете проводить следующим типом продукции: {self.spisok_result_tovar[4].lower()}. "
                f"Ваша кожа требует ухода и {self.spisok_result_tovar[3].lower()}.\n\n"
                f"Все товары выбраны исключительно по Вашим параметрам и характеристках, а также целью ухода: {self.spisok_result_tovar[5].lower()}\n"
                f"Отталкиваясь от всех параметров кожи, можно сделать следующий список рекомендованных продуктов для Вас:")

            select_med = combo_box_1.currentText()
            select_med_tool = combo_box_2.currentText()
            select_med_type = combo_box_5.currentText()
            global label_otvet

            if select_med == "Сухость кожи":

                if select_med_type == 'Крем':
                    label_otvet = QLabel(f"{cream[0]}\n{cream[2]}\n{cream[3]}")

                elif select_med_type == 'Сыворотка':
                    label_otvet = QLabel(f"{serum[2]}")

                elif select_med_type == 'Лосьон':
                    label_otvet = QLabel(f"{lotion[2]}")

                elif select_med_type == 'Тоник':
                    label_otvet = QLabel(f"{tonic[0]}\n{tonic[2]}")

                elif select_med_type == 'Маска':
                    label_otvet = QLabel(f"{mask[0]}\n{mask[3]}\n{mask[1]}")

                elif select_med_type == 'Скраб':
                    label_otvet = QLabel(f"{scrub[0]}\n{scrub[2]}")

                elif select_med_type == 'Мицеллярная вода':
                    label_otvet = QLabel(f"{micellar_water[1]}")

                elif select_med_type == 'Эмульсия':
                    label_otvet = QLabel(f"{emulsion[1]}\n{emulsion[2]}")

                elif select_med_type == 'Гель для умывания':
                    label_otvet = QLabel(f"{Washing_gel[1]}")

            elif select_med == "Ощущения после умывания":

                if select_med_tool == "Чувство стянутости":
                    if select_med_type == 'Крем':
                        label_otvet = QLabel(f"{cream[1]}\n{cream[3]}\n{cream[0]}")

                    elif select_med_type == 'Сыворотка':
                        label_otvet = QLabel(f"{serum[0]}")

                    elif select_med_type == 'Лосьон':
                        label_otvet = QLabel(f"{lotion[2]}\n{lotion[1]}")

                    elif select_med_type == 'Тоник':
                        label_otvet = QLabel(f"{tonic[0]}\n{tonic[1]}\n{tonic[2]}")

                    elif select_med_type == 'Маска':
                        label_otvet = QLabel(f"{mask[2]}\n{mask[4]}\n{mask[1]}")

                    elif select_med_type == 'Скраб':
                        label_otvet = QLabel(f"{scrub[0]}\n{scrub[1]}")

                    elif select_med_type == 'Мицеллярная вода':
                        label_otvet = QLabel(f"{micellar_water[1]}")

                    elif select_med_type == 'Эмульсия':
                        label_otvet = QLabel(f"{emulsion[1]}\n{emulsion[2]}")

                    elif select_med_type == 'Гель для умывания':
                        label_otvet = QLabel(f"{Washing_gel[1]}")
                elif select_med_tool == "Появляется жирный блеск":

                    if select_med_type == 'Крем':
                        label_otvet = QLabel(f"{cream[2]}\n{cream[3]}")

                    elif select_med_type == 'Сыворотка':
                        label_otvet = QLabel(f"{serum[0]}\n{serum[2]}")

                    elif select_med_type == 'Лосьон':
                        label_otvet = QLabel(f"{lotion[2]}\n{lotion[0]}\n{lotion[4]}\n{lotion[6]}")

                    elif select_med_type == 'Тоник':
                        label_otvet = QLabel(f"{tonic[8]}\n{tonic[4]}\n{tonic[1]}\n{tonic[6]}")

                    elif select_med_type == 'Маска':
                        label_otvet = QLabel(f"{mask[0]}\n{mask[3]}\n{mask[1]}\n{mask[6]}\n{mask[9]}\n{mask[8]}")

                    elif select_med_type == 'Скраб':
                        label_otvet = QLabel(f"{scrub[0]}\n{scrub[2]}\n{scrub[5]}\n{scrub[7]}")

                    elif select_med_type == 'Мицеллярная вода':
                        label_otvet = QLabel(f"{micellar_water[1]}\n{micellar_water[10]}\n{micellar_water[6]}")

                    elif select_med_type == 'Эмульсия':
                        label_otvet = QLabel(f"{emulsion[2]}\n{emulsion[5]}\n{emulsion[7]}")

                    elif select_med_type == 'Гель для умывания':
                        label_otvet = QLabel(f"{Washing_gel[1]}\n{Washing_gel[5]}\n{Washing_gel[6]}")
                elif select_med_tool == "Дискомфорт отсутствует":
                    if select_med_type == 'Крем':
                        label_otvet = QLabel(f"{cream[8]}\n{cream[2]}\n{cream[6]}\n{cream[5]}")

                    elif select_med_type == 'Сыворотка':
                        label_otvet = QLabel(f"{serum[2]}\n{serum[5]}\n{serum[7]}\n{serum[9]}")

                    elif select_med_type == 'Лосьон':
                        label_otvet = QLabel(f"{lotion[2]}\n{lotion[5]}\n{lotion[10]}")

                    elif select_med_type == 'Тоник':
                        label_otvet = QLabel(f"{tonic[3]}\n{tonic[8]}")

                    elif select_med_type == 'Маска':
                        label_otvet = QLabel(f"{mask[1]}\n{mask[9]}\n{mask[11]}")

                    elif select_med_type == 'Скраб':
                        label_otvet = QLabel(f"{scrub[0]}\n{scrub[5]}\n{scrub[3]}\n{scrub[2]}")

                    elif select_med_type == 'Мицеллярная вода':
                        label_otvet = QLabel(f"{micellar_water[1]}\n{micellar_water[7]}\n{micellar_water[4]}")

                    elif select_med_type == 'Эмульсия':
                        label_otvet = QLabel(f"{emulsion[5]}\n{emulsion[9]}")

                    elif select_med_type == 'Гель для умывания':
                        label_otvet = QLabel(f"{Washing_gel[1]}\n{Washing_gel[7]}\n{Washing_gel[10]}")

            elif select_med == "Жирный блеск":
                if select_med_type == 'Крем':
                    cream_indices = [0, 2, 4, 6]
                    selected_creams = [cream[i] for i in cream_indices]
                    label_otvet = QLabel('\n'.join(selected_creams))

                elif select_med_type == 'Сыворотка':
                    serum_indices = [1, 3, 5, 7]
                    selected_serums = [serum[i] for i in serum_indices]
                    label_otvet = QLabel('\n'.join(selected_serums))

                elif select_med_type == 'Лосьон':
                    lotion_indices = [8, 9, 10]
                    selected_lotions = [lotion[i] for i in lotion_indices]
                    label_otvet = QLabel('\n'.join(selected_lotions))

                elif select_med_type == 'Тоник':
                    tonic_indices = [3, 5]
                    selected_tonics = [tonic[i] for i in tonic_indices]
                    label_otvet = QLabel('\n'.join(selected_tonics))

                elif select_med_type == 'Маска':
                    mask_indices = [0, 2, 4]
                    selected_masks = [mask[i] for i in mask_indices]
                    label_otvet = QLabel('\n'.join(selected_masks))

                elif select_med_type == 'Скраб':
                    scrub_indices = [1, 3, 5, 7]
                    selected_scrubs = [scrub[i] for i in scrub_indices]
                    label_otvet = QLabel('\n'.join(selected_scrubs))

                elif select_med_type == 'Мицеллярная вода':
                    micellar_indices = [2, 4, 6]
                    selected_micellar_waters = [micellar_water[i] for i in micellar_indices]
                    label_otvet = QLabel('\n'.join(selected_micellar_waters))

                elif select_med_type == 'Эмульсия':
                    emulsion_indices = [0, 2, 4]
                    selected_emulsions = [emulsion[i] for i in emulsion_indices]
                    label_otvet = QLabel('\n'.join(selected_emulsions))

                elif select_med_type == 'Гель для умывания':
                    gel_indices = [1, 3, 5]
                    selected_gels = [Washing_gel[i] for i in gel_indices]
                    label_otvet = QLabel('\n'.join(selected_gels))

            elif select_med == "Поры":
                if select_med_type == 'Крем':
                    cream_indices = [1, 3, 4, 8, 9]
                    selected_creams = [cream[i] for i in cream_indices]
                    label_otvet = QLabel('\n'.join(selected_creams))

                elif select_med_type == 'Сыворотка':
                    serum_indices = [0, 2, 4, 7, 9]
                    selected_serums = [serum[i] for i in serum_indices]
                    label_otvet = QLabel('\n'.join(selected_serums))

                elif select_med_type == 'Лосьон':
                    lotion_indices = [0, 3, 5, 6, 9]
                    selected_lotions = [lotion[i] for i in lotion_indices]
                    label_otvet = QLabel('\n'.join(selected_lotions))

                elif select_med_type == 'Тоник':
                    tonic_indices = [1, 2, 4, 5, 9]
                    selected_tonics = [tonic[i] for i in tonic_indices]
                    label_otvet = QLabel('\n'.join(selected_tonics))

                elif select_med_type == 'Маска':
                    mask_indices = [0, 3, 5, 7, 8]
                    selected_masks = [mask[i] for i in mask_indices]
                    label_otvet = QLabel('\n'.join(selected_masks))

                elif select_med_type == 'Скраб':
                    scrub_indices = [2, 3, 4, 6, 9]
                    selected_scrubs = [scrub[i] for i in scrub_indices]
                    label_otvet = QLabel('\n'.join(selected_scrubs))

                elif select_med_type == 'Мицеллярная вода':
                    micellar_indices = [1, 2, 6, 7, 9]
                    selected_micellar_waters = [micellar_water[i] for i in micellar_indices]
                    label_otvet = QLabel('\n'.join(selected_micellar_waters))

                elif select_med_type == 'Эмульсия':
                    emulsion_indices = [0, 2, 3, 6, 8]
                    selected_emulsions = [emulsion[i] for i in emulsion_indices]
                    label_otvet = QLabel('\n'.join(selected_emulsions))

                elif select_med_type == 'Гель для умывания':
                    gel_indices = [1, 4, 5, 7, 9]
                    selected_gels = [Washing_gel[i] for i in gel_indices]
                    label_otvet = QLabel('\n'.join(selected_gels))

            elif select_med == "Чувствительность":
                if select_med_type == 'Крем':
                    cream_indices = [0, 2, 3, 6, 8]
                    selected_creams = [cream[i] for i in cream_indices]
                    label_otvet = QLabel('\n'.join(selected_creams))

                elif select_med_type == 'Сыворотка':
                    serum_indices = [0, 1, 3, 5, 8]
                    selected_serums = [serum[i] for i in serum_indices]
                    label_otvet = QLabel('\n'.join(selected_serums))

                elif select_med_type == 'Лосьон':
                    lotion_indices = [1, 2, 4, 6, 9]
                    selected_lotions = [lotion[i] for i in lotion_indices]
                    label_otvet = QLabel('\n'.join(selected_lotions))

                elif select_med_type == 'Тоник':
                    tonic_indices = [0, 3, 5, 7, 9]
                    selected_tonics = [tonic[i] for i in tonic_indices]
                    label_otvet = QLabel('\n'.join(selected_tonics))

                elif select_med_type == 'Маска':
                    mask_indices = [1, 2, 4, 6, 9]
                    selected_masks = [mask[i] for i in mask_indices]
                    label_otvet = QLabel('\n'.join(selected_masks))

                elif select_med_type == 'Скраб':
                    scrub_indices = [0, 3, 5, 7, 8]
                    selected_scrubs = [scrub[i] for i in scrub_indices]
                    label_otvet = QLabel('\n'.join(selected_scrubs))

                elif select_med_type == 'Мицеллярная вода':
                    micellar_indices = [0, 2, 4, 6, 9]
                    selected_micellar_waters = [micellar_water[i] for i in micellar_indices]
                    label_otvet = QLabel('\n'.join(selected_micellar_waters))

                elif select_med_type == 'Эмульсия':
                    emulsion_indices = [0, 1, 3, 5, 7]
                    selected_emulsions = [emulsion[i] for i in emulsion_indices]
                    label_otvet = QLabel('\n'.join(selected_emulsions))

                elif select_med_type == 'Гель для умывания':
                    gel_indices = [1, 2, 4, 6, 9]
                    selected_gels = [Washing_gel[i] for i in gel_indices]
                    label_otvet = QLabel('\n'.join(selected_gels))

            elif select_med == "Тон кожи":
                if select_med_type == 'Крем':
                    cream_indices = [0, 2, 3, 6, 8]
                    selected_creams = [cream[i] for i in cream_indices]
                    label_otvet = QLabel('\n'.join(selected_creams))

                elif select_med_type == 'Сыворотка':
                    serum_indices = [0, 1, 3, 5, 8]
                    selected_serums = [serum[i] for i in serum_indices]
                    label_otvet = QLabel('\n'.join(selected_serums))

                elif select_med_type == 'Лосьон':
                    lotion_indices = [0, 1, 4, 5, 7]
                    selected_lotions = [lotion[i] for i in lotion_indices]
                    label_otvet = QLabel('\n'.join(selected_lotions))

                elif select_med_type == 'Тоник':
                    tonic_indices = [2, 3, 4, 5, 7]
                    selected_tonics = [tonic[i] for i in tonic_indices]
                    label_otvet = QLabel('\n'.join(selected_tonics))

                elif select_med_type == 'Маска':
                    mask_indices = [0, 2, 5, 6, 9]
                    selected_masks = [mask[i] for i in mask_indices]
                    label_otvet = QLabel('\n'.join(selected_masks))

                elif select_med_type == 'Скраб':
                    scrub_indices = [1, 3, 4, 7, 8]
                    selected_scrubs = [scrub[i] for i in scrub_indices]
                    label_otvet = QLabel('\n'.join(selected_scrubs))

                elif select_med_type == 'Мицеллярная вода':
                    micellar_indices = [0, 2, 4, 6, 9]
                    selected_micellar_waters = [micellar_water[i] for i in micellar_indices]
                    label_otvet = QLabel('\n'.join(selected_micellar_waters))

                elif select_med_type == 'Эмульсия':
                    emulsion_indices = [1, 2, 4, 5, 7]
                    selected_emulsions = [emulsion[i] for i in emulsion_indices]
                    label_otvet = QLabel('\n'.join(selected_emulsions))

                elif select_med_type == 'Гель для умывания':
                    gel_indices = [0, 3, 6, 8, 10]
                    selected_gels = [Washing_gel[i] for i in gel_indices]
                    label_otvet = QLabel('\n'.join(selected_gels))

            elif select_med == "Морщины":
                if select_med_type == 'Крем':
                    cream_indices = [1, 4, 7, 8, 9]
                    selected_creams = [cream[i] for i in cream_indices]
                    label_otvet = QLabel('\n'.join(selected_creams))

                elif select_med_type == 'Сыворотка':
                    serum_indices = [1, 2, 3, 6, 7]
                    selected_serums = [serum[i] for i in serum_indices]
                    label_otvet = QLabel('\n'.join(selected_serums))

                elif select_med_type == 'Лосьон':
                    lotion_indices = [0, 4, 7, 8, 9]
                    selected_lotions = [lotion[i] for i in lotion_indices]
                    label_otvet = QLabel('\n'.join(selected_lotions))

                elif select_med_type == 'Тоник':
                    tonic_indices = [2, 3, 5, 8, 9]
                    selected_tonics = [tonic[i] for i in tonic_indices]
                    label_otvet = QLabel('\n'.join(selected_tonics))

                elif select_med_type == 'Маска':
                    mask_indices = [3, 4, 5, 6, 8]
                    selected_masks = [mask[i] for i in mask_indices]
                    label_otvet = QLabel('\n'.join(selected_masks))

                elif select_med_type == 'Скраб':
                    scrub_indices = [0, 2, 6, 7, 9]
                    selected_scrubs = [scrub[i] for i in scrub_indices]
                    label_otvet = QLabel('\n'.join(selected_scrubs))

                elif select_med_type == 'Мицеллярная вода':
                    micellar_indices = [0, 1, 4, 6, 7]
                    selected_micellar_waters = [micellar_water[i] for i in micellar_indices]
                    label_otvet = QLabel('\n'.join(selected_micellar_waters))

                elif select_med_type == 'Эмульсия':
                    emulsion_indices = [1, 3, 5, 8, 9]
                    selected_emulsions = [emulsion[i] for i in emulsion_indices]
                    label_otvet = QLabel('\n'.join(selected_emulsions))

                elif select_med_type == 'Гель для умывания':
                    gel_indices = [1, 3, 6, 8, 9]
                    selected_gels = [Washing_gel[i] for i in gel_indices]
                    label_otvet = QLabel('\n'.join(selected_gels))

            label_dopol = QLabel(f"Эти продукты предоставляют всесторонний уход для вашей кожи, помогая сохранить её здоровье и красоту. \n"
                                 f"Независимо они способны увлажнить, питать и поддерживать баланс, необходимый для её оптимального состояния. \n"
                                 f"Выберите эти средства, чтобы достичь и поддерживать здоровое и сияющее состояние кожи.\n")

            label.setAlignment(Qt.AlignLeft | Qt.AlignTop)
            label_otvet.setAlignment(Qt.AlignLeft | Qt.AlignTop)

            project_dir = os.path.dirname(os.path.abspath(__file__))

            # Объедините путь к каталогу проекта с относительными путями к шрифтам
            font_path_italic = os.path.join(project_dir, "fonts", "Montserrat Italic 400.ttf")
            font_path_light = os.path.join(project_dir, "fonts", "Montserrat Light 300.ttf")
            font_path_extra_light = os.path.join(project_dir, "fonts", "Montserrat ExtraLight 275.ttf")
            #
            # Добавьте шрифты к базе данных шрифтов
            font_id_italic = QFontDatabase.addApplicationFont(font_path_italic)
            font_family_italic = QFontDatabase.applicationFontFamilies(font_id_italic)[0]
            custom_font_italic = QFont(font_family_italic, 16)
            #
            font_id_light = QFontDatabase.addApplicationFont(font_path_light)
            font_family_light = QFontDatabase.applicationFontFamilies(font_id_light)[0]
            custom_font_light = QFont(font_family_light, 14)
            #
            font_id_extra_light = QFontDatabase.addApplicationFont(font_path_extra_light)
            font_family_extra_light = QFontDatabase.applicationFontFamilies(font_id_extra_light)[0]
            custom_font_extra_light = QFont(font_family_extra_light, 14)


            label.setFont(custom_font_italic)
            label_otvet.setFont(custom_font_light)
            label_dopol.setFont(custom_font_extra_light)

            label.setStyleSheet("border: 3px solid #333; background-color: #f5f5f5; border-radius: 3px; padding: 5px;")
            label_otvet.setStyleSheet(
                "border: 3px solid #333; background-color: #f5f5f5; border-radius: 3px; padding: 5px;")
            label_dopol.setStyleSheet(
                "border: 3px solid #333; background-color: #f5f5f5; border-radius: 3px; padding: 5px;")

            layout = QVBoxLayout()

            layout.addWidget(label)
            layout.addWidget(label_otvet)
            layout.addWidget(label_dopol)

            dialog.setLayout(layout)
            dialog.exec_()



            # # Style for the dialog background
            # dialog.setStyleSheet("background-color: #EFEFEF;")

        button = QPushButton("Результаты", self)
        button.setStyleSheet(
    "QPushButton {"
    "background-color: #4CAF50;"
    "color: white;"
    "border: none;"
    "border-radius: 35px;"
    "font-size: 18px;"
    "padding: 10px 20px;"
    "min-height: 50px;"
    "}"
    "QPushButton:disabled {"
    "background-color: #45A049;"  # Цвет при нажатии и анимации загрузки
    "}"
)



        button.setFont(QFont("Arial", 12))  # Изменяем шрифт кнопки
        button.clicked.connect(show_selected_text)



        layout_2 = QHBoxLayout()
        layout_2.addWidget(label_2)
        layout_2.addWidget(combo_box_2)

        layout_1 = QHBoxLayout()
        layout_1.addWidget(label_1)
        layout_1.addWidget(combo_box_1)

        layout_3 = QHBoxLayout()
        layout_3.addWidget(label_3)
        layout_3.addWidget(combo_box_3)

        layout_4 = QHBoxLayout()
        layout_4.addWidget(label_4)
        layout_4.addWidget(combo_box_4)

        layout_5 = QHBoxLayout()
        layout_5.addWidget(label_5)
        layout_5.addWidget(combo_box_5)

        layout_6 = QHBoxLayout()
        layout_6.addWidget(label_6)
        layout_6.addWidget(combo_box_6)

        main_layout.addLayout(layout_1)
        main_layout.addLayout(layout_2)
        main_layout.addLayout(layout_3)
        main_layout.addLayout(layout_4)
        main_layout.addLayout(layout_5)
        main_layout.addLayout(layout_6)
        main_layout.addWidget(button)

        return main_layout


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CosmeticsSelectorApp()
    window.show()
    sys.exit(app.exec_())
