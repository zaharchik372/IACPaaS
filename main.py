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
            "Чувствительная",
            "Комбинированная"])

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
                "Активная сыворотка с маслом ши и витамином Е для питания и восстановления кожи",
                "Двухфазная сыворотка для интенсивного увлажнения и поддержания баланса воды",
                "Антиоксидантная сыворотка 'Сияние и защита от окружающей среды'",
                "Сыворотка с морским коллагеном для упругости и улучшения овала лица",
                "Комплексная сыворотка с витамином С и гиалуроновой кислотой",
                "Сыворотка с маслом авокадо для интенсивного питания сухой кожи",
                "Сыворотка с экстрактом зеленого чая для снятия воспалений и покраснений",
                "Активатор клеточной регенерации 'Лифтинг и восстановление'",
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
                     "Освежающий тоник с ментоловым экстрактом 'Аромат свежести'",
                     "Тоник для лица с маслом шиповника и ромашкой 'Успокоение и питание'",
                     "Минеральный тоник с водой из ледникового источника для увлажнения",
                     "Тоник с гиалуроновой кислотой и витамином Е 'Интенсивное увлажнение'",
                     "Тоник с экстрактом лаванды для расслабления и улучшения сна кожи",
                     "Тоник с морским кальцием для укрепления кожи и предотвращения потери упругости"
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
                    "Маска-пилинг с фруктовыми кислотами для мягкого отшелушивания",
                    "Маска с экстрактом женьшеня для тонизирования и упругости кожи",
                    "Маска-гель с гиалуроновой кислотой для интенсивного увлажнения",
                    "Маска с маслом шиповника для питания и восстановления кожи",
                    "Маска с ментоловым эффектом для ощущения свежести и чистоты"
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
                     "Энергетический скраб с экстрактом зеленого чая для тонизирования кожи",
                     "Антицеллюлитный скраб с розовым гималайским солью",
                     "Скраб с маслом арганы и медом для питания и увлажнения",
                     "Детокс скраб с углем и эфирными маслами для глубокого очищения",
                     "Скраб для лица и тела с маслами авокадо и макадамии",
                     "Скраб с фруктовыми кислотами для мягкого пилинга и обновления"
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
                              "Мицеллярная вода для снятия макияжа 'Восстановление и увлажнение'",
                              "Очищающая мицеллярная вода с экстрактом огурца для ухода за нормальной кожей",
                              "Мицеллярная вода 'Антиоксидантная защита' для борьбы со стрессом кожи",
                              "Успокаивающая мицеллярная вода с маслом шиповника для чувствительной кожи",
                              "Мицеллярная вода с витамином С для сияющей и здоровой кожи",
                              "Мицеллярная вода для лица и глаз 'Деликатное очищение и тонизирование'"
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
                        "Эмульсия с экстрактом зеленого чая для освежения и защиты кожи",
                        "Легкая восстанавливающая эмульсия 'Лавандовый расслабляющий уход'",
                        "Увлажняющая эмульсия 'Цитрусовый аромат свежести'",
                        "Эмульсия для жирной кожи с антиоксидантами и экстрактом грейпфрута",
                        "Легкая восстанавливающая эмульсия 'Оливковое увлажнение'",
                        "Увлажняющая эмульсия 'Тропическое увлажнение'",
                        "Эмульсия с ромашкой для чувствительной кожи",
                        "Матирующая эмульсия с экстрактом бамбука для контроля блеска",
                        "Эмульсия для нормализации работы сальных желез с экстрактом чайного дерева",
                        "Антивозрастная эмульсия с маслами авокадо и ши"
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
                           "Очищающий гель с ментоловым эффектом 'Арктическая свежесть'",
                           "Тонизирующий гель-уход с экстрактом зеленого чая",
                           "Очищающий гель для снятия макияжа 'Энергия цитрусовых'",
                           "Деликатный гель с алое вера и маслом шиповника для чувствительной кожи",
                           "Увлажняющий гель-масло для интенсивного увлажнения и питания",
                           "Очищающий гель для лица с гидрофильным маслом и витамином E",
                           "Гель для умывания с антивозрастным комплексом 'Цветущая молодость'",
                           "Очищающий гель с микрогранулами для глубокого очищения пор",
                           "Гель для умывания с витамином С для яркости и сияния кожи",
                           "Очищающий гель с экстрактом лайма для свежести и тонуса"
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

            select_score_1 = combo_box_1.currentText()
            select_tool_2 = combo_box_2.currentText()
            select_type_3 = combo_box_3.currentText()
            select_med_type_5 = combo_box_5.currentText()
            global label_otvet

            if select_score_1 == 'Сухость кожи':
                # Тип кожи
                if select_type_3 == 'Сухая':
                    # Характеристика
                    if select_tool_2 == 'На коже есть шелушения':
                        # Уходовые средства
                        if select_med_type_5 == 'Крем':
                            cream_indices = [1, 3, 5, 7]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [2, 4, 6, 8]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [0, 4, 7, 8, 9]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        # Аналогично обработайте другие виды ухода
                        elif select_med_type_5 == 'Тоник':
                            tonic_indices = [0, 2, 5, 8]
                            selected_items = [tonic[i] for i in tonic_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [1, 3, 6, 9]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [0, 2, 5, 8]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_water_indices = [1, 4, 6, 9]
                            selected_items = [micellar_water[i] for i in micellar_water_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [0, 3, 5, 8, 9]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            washing_gel_indices = [1, 4, 7, 9]
                            selected_items = [Washing_gel[i] for i in washing_gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                    elif select_tool_2 == 'Шелушения отсутствуют, кожа достаточно увлажнена':
                        # Уходовые средства
                        if select_med_type_5 == 'Крем':
                            cream_indices = [0, 2, 4, 6]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [1, 3, 5, 7]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [2, 5, 8, 9]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        # Аналогично обработайте другие виды ухода
                        elif select_med_type_5 == 'Тоник':
                            tonic_indices = [1, 4, 7, 9]
                            selected_items = [tonic[i] for i in tonic_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [0, 2, 5, 8]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [1, 4, 7, 9]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_water_indices = [0, 3, 5, 8]
                            selected_items = [micellar_water[i] for i in micellar_water_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [2, 4, 7, 9]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            washing_gel_indices = [0, 3, 6, 8]
                            selected_items = [Washing_gel[i] for i in washing_gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                elif select_type_3 == 'Жирная':
                    # Характеристика
                    if select_tool_2 == 'На коже есть шелушения':
                        # Уходовые средства
                        if select_med_type_5 == 'Крем':
                            cream_indices = [0, 2, 4, 6]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [1, 3, 5, 7]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [2, 5, 8, 9]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Тоник':
                            tonic_indices = [1, 4, 7, 9]
                            selected_items = [tonic[i] for i in tonic_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [0, 2, 5, 8]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [1, 4, 7, 9]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_water_indices = [0, 3, 5, 8]
                            selected_items = [micellar_water[i] for i in micellar_water_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [2, 4, 7, 9]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            washing_gel_indices = [0, 3, 6, 8]
                            selected_items = [Washing_gel[i] for i in washing_gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                    elif select_tool_2 == 'Шелушения отсутствуют, кожа достаточно увлажнена':
                        # Уходовые средства
                        if select_med_type_5 == 'Крем':
                            cream_indices = [1, 5, 7, 8]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [2, 3, 1, 10]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [1, 3, 4, 8]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        # Аналогично обработайте другие виды ухода
                        elif select_med_type_5 == 'Тоник':
                            tonic_indices = [1, 2, 10, 4]
                            selected_items = [tonic[i] for i in tonic_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [0, 2, 5, 8]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [2, 12, 7, 8]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_water_indices = [1, 4, 8, 10]
                            selected_items = [micellar_water[i] for i in micellar_water_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [1, 2, 5, 8]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            washing_gel_indices = [1, 2, 7, 8]
                            selected_items = [Washing_gel[i] for i in washing_gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                if select_type_3 == 'Нормальная':
                    # Характеристика
                    if select_tool_2 == 'На коже есть шелушения':
                        # Уходовые средства
                        if select_med_type_5 == 'Крем':
                            cream_indices = [0, 2, 4, 6]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [1, 3, 5, 7]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [2, 5, 8, 9]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Тоник':
                            tonic_indices = [1, 4, 7, 9]
                            selected_items = [tonic[i] for i in tonic_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [0, 2, 5, 8]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [1, 4, 7, 9]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_water_indices = [0, 3, 5, 8]
                            selected_items = [micellar_water[i] for i in micellar_water_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [2, 4, 7, 9]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            washing_gel_indices = [0, 3, 6, 8]
                            selected_items = [Washing_gel[i] for i in washing_gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                    if select_tool_2 == 'Шелушения отсутствуют, кожа достаточно увлажнена':
                        # Уходовые средства
                        if select_med_type_5 == 'Крем':
                            cream_indices = [1, 3, 5, 7]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [2, 4, 6, 8]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [1, 5, 8, 9]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Тоник':
                            tonic_indices = [0, 3, 5, 8]
                            selected_items = [tonic[i] for i in tonic_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [1, 4, 7, 9]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [0, 3, 6, 8]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_water_indices = [1, 4, 7, 9]
                            selected_items = [micellar_water[i] for i in micellar_water_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [0, 2, 5, 8]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            washing_gel_indices = [1, 3, 6, 8]
                            selected_items = [Washing_gel[i] for i in washing_gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                if select_type_3 == 'Чувствительная':
                    # Характеристика
                    if select_tool_2 == 'На коже есть шелушения':
                        # Уходовые средства
                        if select_med_type_5 == 'Крем':
                            cream_indices = [1, 3, 5, 7]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [2, 4, 6, 8]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [0, 4, 7, 8, 9]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Тоник':
                            toner_indices = [1, 3, 5, 7]
                            selected_items = [tonic[i] for i in toner_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [0, 2, 4, 6]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [1, 3, 5, 7]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_indices = [0, 3, 5, 8]
                            selected_items = [micellar_water[i] for i in micellar_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [1, 3, 5, 8, 9]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            gel_indices = [1, 3, 6, 8, 9]
                            selected_items = [Washing_gel[i] for i in gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                    elif select_tool_2 == 'Шелушения отсутствуют, кожа достаточно увлажнена':
                        if select_med_type_5 == 'Крем':
                            cream_indices = [1, 4, 7, 9, 11]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [0, 2, 5, 8, 10, 12]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [3, 6, 9]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Тоник':
                            toner_indices = [2, 5, 7, 10]
                            selected_items = [tonic[i] for i in toner_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [0, 4, 6, 9, 12]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [1, 3, 8, 11]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_indices = [2, 5, 8, 11, 12]
                            selected_items = [micellar_water[i] for i in micellar_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [0, 3, 7, 9, 11]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            gel_indices = [1, 4, 6, 8, 10]
                            selected_items = [Washing_gel[i] for i in gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                if select_type_3 == 'Комбинированная':
                    # Характеристика
                    if select_tool_2 == 'На коже есть шелушения':
                        # Уходовые средства
                        if select_med_type_5 == 'Крем':
                            cream_indices = [1, 3, 5, 7]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [2, 4, 6, 8]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [1, 5, 8, 9]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Тоник':
                            toner_indices = [0, 3, 6, 9]
                            selected_items = [tonic[i] for i in toner_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [2, 4, 7, 11]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [0, 2, 5, 8]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_indices = [1, 4, 7]
                            selected_items = [micellar_water[i] for i in micellar_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [0, 3, 5, 9]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            gel_indices = [2, 5, 8, 10]
                            selected_items = [Washing_gel[i] for i in gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                    if select_tool_2 == 'Шелушения отсутствуют, кожа достаточно увлажнена':
                        # Уходовые средства
                        if select_med_type_5 == 'Крем':
                            cream_indices = [0, 2, 5, 7, 9, 11]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [1, 4, 6, 8, 10]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [0, 3, 5, 8, 10]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Тоник':
                            toner_indices = [1, 4, 6, 9, 11]
                            selected_items = [tonic[i] for i in toner_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [0, 2, 5, 7, 10]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [1, 3, 6, 9, 11]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_indices = [0, 2, 5, 7, 10]
                            selected_items = [micellar_water[i] for i in micellar_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [1, 4, 7, 9, 11]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            gel_indices = [0, 3, 5, 8, 10]
                            selected_items = [Washing_gel[i] for i in gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
            elif select_score_1 == 'Ощущения после умывания':
                if select_type_3 == "Сухая":
                    if select_tool_2 == "Чувство стянутости":
                        if select_med_type_5 == 'Крем':
                            cream_indices = [0, 2, 5, 7, 10]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [1, 3, 6, 8, 11]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [0, 2, 5, 8, 11]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Тоник':
                            toner_indices = [1, 3, 6, 9, 12]
                            selected_items = [tonic[i] for i in toner_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [0, 2, 5, 7, 10]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [1, 3, 6, 9, 12]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_indices = [0, 2, 5, 7, 10]
                            selected_items = [micellar_water[i] for i in micellar_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [1, 4, 7, 9, 12]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            gel_indices = [0, 3, 6, 9, 12]
                            selected_items = [Washing_gel[i] for i in gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                    elif select_tool_2 == "Появляется жирный блеск":
                        if select_med_type_5 == 'Крем':
                            cream_indices = [1, 3, 6, 8, 11]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [0, 2, 5, 7, 10]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [1, 4, 7, 9, 12]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Тоник':
                            toner_indices = [0, 3, 6, 8, 11]
                            selected_items = [tonic[i] for i in toner_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [1, 3, 6, 9, 11]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [0, 2, 5, 8, 10]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_indices = [1, 4, 7, 9, 12]
                            selected_items = [micellar_water[i] for i in micellar_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [0, 2, 5, 8, 11]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            gel_indices = [1, 3, 6, 9, 12]
                            selected_items = [Washing_gel[i] for i in gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                    elif select_tool_2 == "Дискомфорт отсутствует":
                        if select_med_type_5 == 'Крем':
                            cream_indices = [0, 3, 6, 8, 11]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [1, 4, 7, 9, 12]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [0, 2, 5, 8, 10]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Тоник':
                            toner_indices = [1, 3, 6, 9, 11]
                            selected_items = [tonic[i] for i in toner_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [0, 2, 5, 7, 10]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [1, 4, 7, 9, 11]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_indices = [0, 3, 6, 8, 12]
                            selected_items = [micellar_water[i] for i in micellar_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [1, 2, 5, 8, 11]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            gel_indices = [0, 3, 6, 9, 10]
                            selected_items = [Washing_gel[i] for i in gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                elif select_type_3 == "Жирная":
                    if select_tool_2 == "Чувство стянутости":
                        if select_med_type_5 == 'Крем':
                            cream_indices = [0, 3, 6, 9, 12]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [1, 4, 7, 10, 11]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [0, 2, 5, 8, 11]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Тоник':
                            toner_indices = [1, 3, 6, 9, 12]
                            selected_items = [tonic[i] for i in toner_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [0, 3, 5, 8, 11]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [1, 4, 7, 10, 11]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_indices = [0, 2, 5, 8, 12]
                            selected_items = [micellar_water[i] for i in micellar_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [1, 3, 6, 9, 10]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            gel_indices = [0, 3, 6, 9, 11]
                            selected_items = [Washing_gel[i] for i in gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                    elif select_tool_2 == "Появляется жирный блеск":
                        if select_med_type_5 == 'Крем':
                            cream_indices = [1, 4, 7, 10, 11]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [0, 3, 6, 9, 12]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [1, 4, 7, 10, 11]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Тоник':
                            toner_indices = [0, 3, 6, 9, 12]
                            selected_items = [tonic[i] for i in toner_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [1, 3, 5, 8, 10]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [0, 2, 6, 9, 11]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_indices = [1, 4, 7, 10, 11]
                            selected_items = [micellar_water[i] for i in micellar_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [0, 2, 5, 8, 11]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            gel_indices = [1, 3, 6, 9, 12]
                            selected_items = [Washing_gel[i] for i in gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))

                    elif select_tool_2 == "Дискомфорт отсутствует":
                        if select_med_type_5 == 'Крем':
                            cream_indices = [0, 3, 6, 9, 11]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [1, 4, 7, 10, 12]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [0, 2, 5, 8, 11]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Тоник':
                            toner_indices = [1, 3, 6, 9, 11]
                            selected_items = [tonic[i] for i in toner_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [0, 3, 5, 8, 10]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [1, 4, 7, 10, 12]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_indices = [0, 2, 5, 8, 11]
                            selected_items = [micellar_water[i] for i in micellar_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [1, 3, 6, 9, 12]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            gel_indices = [0, 3, 6, 9, 11]
                            selected_items = [Washing_gel[i] for i in gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))

                elif select_type_3 == "Нормальная":
                    if select_tool_2 == "Чувство стянутости":
                        if select_med_type_5 == 'Крем':
                            cream_indices = [1, 3, 6, 9, 12]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [0, 4, 7, 10, 11]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [1, 3, 6, 8, 11]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Тоник':
                            toner_indices = [0, 3, 6, 9, 11]
                            selected_items = [tonic[i] for i in toner_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [1, 3, 5, 8, 10]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [0, 2, 5, 8, 11]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_indices = [1, 4, 7, 10, 12]
                            selected_items = [micellar_water[i] for i in micellar_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [0, 2, 5, 8, 11]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            gel_indices = [1, 3, 6, 9, 10]
                            selected_items = [Washing_gel[i] for i in gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))

                    elif select_tool_2 == "Появляется жирный блеск":
                        if select_med_type_5 == 'Крем':
                            cream_indices = [0, 3, 6, 9, 11]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [1, 4, 7, 10, 12]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [0, 2, 5, 8, 11]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Тоник':
                            toner_indices = [1, 3, 6, 9, 12]
                            selected_items = [tonic[i] for i in toner_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [0, 3, 5, 8, 10]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [1, 4, 7, 10, 11]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_indices = [0, 2, 5, 8, 11]
                            selected_items = [micellar_water[i] for i in micellar_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [1, 3, 6, 9, 12]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            gel_indices = [0, 3, 6, 9, 11]
                            selected_items = [Washing_gel[i] for i in gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))

                    elif select_tool_2 == "Дискомфорт отсутствует":
                        if select_med_type_5 == 'Крем':
                            cream_indices = [1, 4, 7, 10, 12]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [0, 3, 6, 9, 11]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [1, 4, 7, 10, 11]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Тоник':
                            toner_indices = [0, 3, 6, 9, 12]
                            selected_items = [tonic[i] for i in toner_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [1, 3, 5, 8, 10]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [0, 2, 5, 8, 11]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_indices = [1, 4, 7, 10, 11]
                            selected_items = [micellar_water[i] for i in micellar_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [0, 2, 5, 8, 11]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            gel_indices = [1, 3, 6, 9, 10]
                            selected_items = [Washing_gel[i] for i in gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))

                elif select_type_3 == "Чувствительная":
                    if select_tool_2 == "Чувство стянутости":
                        if select_med_type_5 == 'Крем':
                            cream_indices = [0, 3, 6, 9, 11]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [1, 4, 7, 10, 12]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [0, 3, 6, 8, 11]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Тоник':
                            toner_indices = [1, 3, 6, 9, 12]
                            selected_items = [tonic[i] for i in toner_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [0, 2, 5, 8, 10]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [1, 4, 7, 10, 11]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_indices = [0, 2, 5, 8, 11]
                            selected_items = [micellar_water[i] for i in micellar_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [1, 3, 6, 9, 11]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            gel_indices = [0, 3, 6, 9, 12]
                            selected_items = [Washing_gel[i] for i in gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))

                    elif select_tool_2 == "Появляется жирный блеск":
                        if select_med_type_5 == 'Крем':
                            cream_indices = [1, 4, 7, 10, 12]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [0, 3, 6, 9, 11]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [1, 4, 7, 10, 11]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Тоник':
                            toner_indices = [0, 3, 6, 9, 12]
                            selected_items = [tonic[i] for i in toner_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [1, 3, 5, 8, 10]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [0, 2, 5, 8, 11]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_indices = [1, 4, 7, 10, 11]
                            selected_items = [micellar_water[i] for i in micellar_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [0, 2, 5, 8, 11]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            gel_indices = [1, 3, 6, 9, 10]
                            selected_items = [Washing_gel[i] for i in gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))

                    elif select_tool_2 == "Дискомфорт отсутствует":
                        if select_med_type_5 == 'Крем':
                            cream_indices = [0, 3, 6, 9, 11]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [1, 4, 7, 10, 12]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [0, 3, 6, 8, 11]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Тоник':
                            toner_indices = [1, 3, 6, 9, 12]
                            selected_items = [tonic[i] for i in toner_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [0, 2, 5, 8, 10]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [1, 4, 7, 10, 11]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_indices = [0, 2, 5, 8, 11]
                            selected_items = [micellar_water[i] for i in micellar_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [1, 3, 6, 9, 12]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            gel_indices = [0, 3, 6, 9, 11]
                            selected_items = [Washing_gel[i] for i in gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))

                elif select_type_3 == "Комбинированная":
                    if select_tool_2 == "Чувство стянутости":
                        if select_med_type_5 == 'Крем':
                            cream_indices = [1, 4, 7, 10, 12]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [0, 3, 6, 9, 11]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [1, 4, 7, 10, 11]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Тоник':
                            toner_indices = [0, 3, 6, 9, 12]
                            selected_items = [tonic[i] for i in toner_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [1, 3, 5, 8, 10]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [0, 2, 5, 8, 11]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_indices = [1, 4, 7, 10, 11]
                            selected_items = [micellar_water[i] for i in micellar_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [0, 2, 5, 8, 11]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            gel_indices = [1, 3, 6, 9, 10]
                            selected_items = [Washing_gel[i] for i in gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))

                    elif select_tool_2 == "Появляется жирный блеск":
                        if select_med_type_5 == 'Крем':
                            cream_indices = [0, 3, 6, 9, 12]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [1, 4, 7, 10, 11]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [0, 3, 6, 8, 11]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Тоник':
                            toner_indices = [1, 3, 6, 9, 12]
                            selected_items = [tonic[i] for i in toner_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [0, 2, 5, 8, 10]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [1, 4, 7, 10, 11]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_indices = [0, 2, 5, 8, 11]
                            selected_items = [micellar_water[i] for i in micellar_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [1, 3, 6, 9, 12]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            gel_indices = [0, 3, 6, 9, 10]
                            selected_items = [Washing_gel[i] for i in gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                    elif select_tool_2 == "Дискомфорт отсутствует":
                        if select_med_type_5 == 'Крем':
                            cream_indices = [1, 4, 7, 10, 11]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [0, 3, 6, 9, 12]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [1, 4, 7, 10, 11]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Тоник':
                            toner_indices = [0, 3, 6, 9, 12]
                            selected_items = [tonic[i] for i in toner_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [1, 3, 5, 8, 10]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [0, 2, 5, 8, 11]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_indices = [1, 4, 7, 10, 12]
                            selected_items = [micellar_water[i] for i in micellar_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [0, 2, 5, 8, 11]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            gel_indices = [1, 3, 6, 9, 10]
                            selected_items = [Washing_gel[i] for i in gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))

            elif select_score_1 == 'Жирный блеск':
                if select_type_3 == "Сухая":
                    if select_tool_2 == "Жирный блеск отсутствует":
                        if select_med_type_5 == 'Крем':
                            cream_indices = [0, 3, 6, 9, 12]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [1, 4, 7, 10, 11]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [0, 3, 6, 8, 11]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Тоник':
                            toner_indices = [1, 3, 6, 9, 12]
                            selected_items = [tonic[i] for i in toner_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [0, 2, 5, 8, 10]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [1, 4, 7, 10, 11]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_indices = [0, 2, 5, 8, 11]
                            selected_items = [micellar_water[i] for i in micellar_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [1, 3, 6, 9, 12]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            gel_indices = [0, 3, 6, 9, 10]
                            selected_items = [Washing_gel[i] for i in gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))

                    elif select_tool_2 == "Слабый, в области Т-зоны (лоб, нос, подбородок)":
                        if select_med_type_5 == 'Крем':
                            cream_indices = [1, 4, 7, 10, 12]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [0, 3, 6, 9, 11]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [1, 4, 7, 10, 11]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Тоник':
                            toner_indices = [0, 3, 6, 9, 12]
                            selected_items = [tonic[i] for i in toner_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [1, 3, 5, 8, 10]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [0, 2, 5, 8, 11]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_indices = [1, 4, 7, 10, 11]
                            selected_items = [micellar_water[i] for i in micellar_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [0, 2, 5, 8, 11]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            gel_indices = [1, 3, 6, 9, 10]
                            selected_items = [Washing_gel[i] for i in gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))

                    elif select_tool_2 == "Заметный блеск на всём лице":
                        if select_med_type_5 == 'Крем':
                            cream_indices = [0, 3, 6, 9, 12]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [1, 4, 7, 10, 11]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [0, 3, 6, 8, 11]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Тоник':
                            toner_indices = [1, 3, 6, 9, 12]
                            selected_items = [tonic[i] for i in toner_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [0, 2, 5, 8, 10]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [1, 4, 7, 10, 11]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_indices = [0, 2, 5, 8, 11]
                            selected_items = [micellar_water[i] for i in micellar_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [1, 3, 6, 9, 12]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            gel_indices = [0, 3, 6, 9, 10]
                            selected_items = [Washing_gel[i] for i in gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))

                elif select_type_3 == "Жирная":
                    if select_tool_2 == "Жирный блеск отсутствует":
                        if select_med_type_5 == 'Крем':
                            cream_indices = [1, 4, 7, 10, 11]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [0, 3, 6, 9, 12]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [1, 4, 7, 10, 11]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Тоник':
                            toner_indices = [0, 3, 6, 9, 12]
                            selected_items = [tonic[i] for i in toner_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [1, 3, 5, 8, 10]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [0, 2, 5, 8, 11]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_indices = [1, 4, 7, 10, 11]
                            selected_items = [micellar_water[i] for i in micellar_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [0, 2, 5, 8, 11]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            gel_indices = [1, 3, 6, 9, 10]
                            selected_items = [Washing_gel[i] for i in gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))

                    elif select_tool_2 == "Слабый, в области Т-зоны (лоб, нос, подбородок)":
                        if select_med_type_5 == 'Крем':
                            cream_indices = [0, 3, 6, 9, 11]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [1, 4, 7, 10, 12]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [0, 3, 6, 8, 11]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Тоник':
                            toner_indices = [1, 3, 6, 9, 12]
                            selected_items = [tonic[i] for i in toner_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [0, 2, 5, 8, 10]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [1, 4, 7, 10, 11]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_indices = [0, 2, 5, 8, 11]
                            selected_items = [micellar_water[i] for i in micellar_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [1, 3, 6, 9, 12]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            gel_indices = [0, 3, 6, 9, 10]
                            selected_items = [Washing_gel[i] for i in gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))

                    elif select_tool_2 == "Заметный блеск на всём лице":
                        if select_med_type_5 == 'Крем':
                            cream_indices = [1, 4, 7, 10, 11]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [0, 3, 6, 9, 12]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [1, 4, 7, 10, 11]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Тоник':
                            toner_indices = [0, 3, 6, 9, 12]
                            selected_items = [tonic[i] for i in toner_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [1, 3, 5, 8, 10]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [0, 2, 5, 8, 11]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_indices = [1, 4, 7, 10, 11]
                            selected_items = [micellar_water[i] for i in micellar_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [0, 2, 5, 8, 11]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            gel_indices = [1, 3, 6, 9, 10]
                            selected_items = [Washing_gel[i] for i in gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))

                elif select_type_3 == "Нормальная":
                    if select_tool_2 == "Жирный блеск отсутствует":
                        if select_med_type_5 == 'Крем':
                            cream_indices = [0, 3, 6, 9, 12]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [1, 4, 7, 10, 11]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [0, 3, 6, 8, 11]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Тоник':
                            toner_indices = [1, 3, 6, 9, 12]
                            selected_items = [tonic[i] for i in toner_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [0, 2, 5, 8, 10]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [1, 4, 7, 10, 11]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_indices = [0, 2, 5, 8, 11]
                            selected_items = [micellar_water[i] for i in micellar_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [1, 3, 6, 9, 12]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            gel_indices = [0, 3, 6, 9, 10]
                            selected_items = [Washing_gel[i] for i in gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                    elif select_tool_2 == "Слабый, в области Т-зоны (лоб, нос, подбородок)":
                        if select_med_type_5 == 'Крем':
                            cream_indices = [1, 4, 7, 10, 11]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [0, 3, 6, 9, 12]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [1, 4, 7, 10, 11]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Тоник':
                            toner_indices = [0, 3, 6, 9, 12]
                            selected_items = [tonic[i] for i in toner_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [1, 3, 5, 8, 10]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [0, 2, 5, 8, 11]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_indices = [1, 4, 7, 10, 11]
                            selected_items = [micellar_water[i] for i in micellar_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [0, 2, 5, 8, 11]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            gel_indices = [1, 3, 6, 9, 10]
                            selected_items = [Washing_gel[i] for i in gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))

                    elif select_tool_2 == "Заметный блеск на всём лице":
                        if select_med_type_5 == 'Крем':
                            cream_indices = [0, 3, 6, 9, 12]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [1, 4, 7, 10, 11]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [0, 3, 6, 8, 11]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Тоник':
                            toner_indices = [1, 3, 6, 9, 12]
                            selected_items = [tonic[i] for i in toner_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [0, 2, 5, 8, 10]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [1, 4, 7, 10, 11]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_indices = [0, 2, 5, 8, 11]
                            selected_items = [micellar_water[i] for i in micellar_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [1, 3, 6, 9, 12]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            gel_indices = [0, 3, 6, 9, 10]
                            selected_items = [Washing_gel[i] for i in gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))

                elif select_type_3 == "Чувствительная":
                    if select_tool_2 == "Жирный блеск отсутствует":
                        if select_med_type_5 == 'Крем':
                            cream_indices = [1, 4, 7, 10, 12]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [0, 3, 6, 9, 11]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [1, 4, 7, 10, 11]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Тоник':
                            toner_indices = [0, 3, 6, 9, 12]
                            selected_items = [tonic[i] for i in toner_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [1, 3, 5, 8, 10]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [0, 2, 5, 8, 11]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_indices = [1, 4, 7, 10, 11]
                            selected_items = [micellar_water[i] for i in micellar_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [0, 2, 5, 8, 11]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            gel_indices = [1, 3, 6, 9, 10]
                            selected_items = [Washing_gel[i] for i in gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))

                    elif select_tool_2 == "Слабый, в области Т-зоны (лоб, нос, подбородок)":
                        if select_med_type_5 == 'Крем':
                            cream_indices = [0, 3, 6, 9, 11]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [1, 4, 7, 10, 12]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [0, 3, 6, 8, 11]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Тоник':
                            toner_indices = [1, 3, 6, 9, 12]
                            selected_items = [tonic[i] for i in toner_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [0, 2, 5, 8, 10]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [1, 4, 7, 10, 11]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_indices = [0, 2, 5, 8, 11]
                            selected_items = [micellar_water[i] for i in micellar_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [1, 3, 6, 9, 12]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            gel_indices = [0, 3, 6, 9, 10]
                            selected_items = [Washing_gel[i] for i in gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))

                    elif select_tool_2 == "Заметный блеск на всём лице":
                        if select_med_type_5 == 'Крем':
                            cream_indices = [1, 4, 7, 10, 12]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [0, 3, 6, 9, 11]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [1, 4, 7, 10, 11]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Тоник':
                            toner_indices = [0, 3, 6, 9, 12]
                            selected_items = [tonic[i] for i in toner_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [1, 3, 5, 8, 10]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [0, 2, 5, 8, 11]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_indices = [1, 4, 7, 10, 11]
                            selected_items = [micellar_water[i] for i in micellar_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [0, 2, 5, 8, 11]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            gel_indices = [1, 3, 6, 9, 10]
                            selected_items = [Washing_gel[i] for i in gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))

                elif select_type_3 == "Комбинированная":
                    if select_tool_2 == "Жирный блеск отсутствует":
                        if select_med_type_5 == 'Крем':
                            cream_indices = [0, 3, 6, 9, 11]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [1, 4, 7, 10, 12]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [0, 3, 6, 8, 11]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Тоник':
                            toner_indices = [1, 3, 6, 9, 12]
                            selected_items = [tonic[i] for i in toner_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [0, 2, 5, 8, 10]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [1, 4, 7, 10, 11]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_indices = [0, 2, 5, 8, 11]
                            selected_items = [micellar_water[i] for i in micellar_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [1, 3, 6, 9, 12]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            gel_indices = [0, 3, 6, 9, 10]
                            selected_items = [Washing_gel[i] for i in gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))

                    elif select_tool_2 == "Слабый, в области Т-зоны (лоб, нос, подбородок)":
                        if select_med_type_5 == 'Крем':
                            cream_indices = [1, 4, 7, 10, 12]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [0, 3, 6, 9, 11]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [1, 4, 7, 10, 11]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Тоник':
                            toner_indices = [0, 3, 6, 9, 12]
                            selected_items = [tonic[i] for i in toner_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [1, 3, 5, 8, 10]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [0, 2, 5, 8, 11]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_indices = [1, 4, 7, 10, 11]
                            selected_items = [micellar_water[i] for i in micellar_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [0, 2, 5, 8, 11]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            gel_indices = [1, 3, 6, 9, 10]
                            selected_items = [Washing_gel[i] for i in gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))

                    elif select_tool_2 == "Заметный блеск на всём лице":
                        if select_med_type_5 == 'Крем':
                            cream_indices = [0, 3, 6, 9, 11]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [1, 4, 7, 10, 12]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [0, 3, 6, 8, 11]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Тоник':
                            toner_indices = [1, 3, 6, 9, 12]
                            selected_items = [tonic[i] for i in toner_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [0, 2, 5, 8, 10]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [1, 4, 7, 10, 11]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_indices = [0, 2, 5, 8, 11]
                            selected_items = [micellar_water[i] for i in micellar_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [1, 3, 6, 9, 12]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            gel_indices = [0, 3, 6, 9, 10]
                            selected_items = [Washing_gel[i] for i in gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))

            elif select_score_1 == 'Поры':
                if select_type_3 == "Сухая":
                    if select_tool_2 == "Узкие, незаметные":
                        if select_med_type_5 == 'Крем':
                            cream_indices = [1, 4, 7, 10, 12]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [0, 3, 6, 9, 11]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [1, 4, 7, 10, 11]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Тоник':
                            toner_indices = [0, 3, 6, 9, 12]
                            selected_items = [tonic[i] for i in toner_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [1, 3, 5, 8, 10]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [0, 2, 5, 8, 11]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_indices = [1, 4, 7, 10, 11]
                            selected_items = [micellar_water[i] for i in micellar_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [0, 2, 5, 8, 11]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            gel_indices = [1, 3, 6, 9, 10]
                            selected_items = [Washing_gel[i] for i in gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))

                    elif select_tool_2 == "Расширенные":
                        if select_med_type_5 == 'Крем':
                            cream_indices = [0, 3, 6, 9, 11]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [1, 4, 7, 10, 12]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [0, 3, 6, 8, 11]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Тоник':
                            toner_indices = [1, 3, 6, 9, 12]
                            selected_items = [tonic[i] for i in toner_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [0, 2, 5, 8, 10]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [1, 4, 7, 10, 11]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_indices = [0, 2, 5, 8, 11]
                            selected_items = [micellar_water[i] for i in micellar_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [1, 3, 6, 9, 12]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            gel_indices = [0, 3, 6, 9, 10]
                            selected_items = [Washing_gel[i] for i in gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))

                elif select_type_3 == "Жирная":
                    if select_tool_2 == "Узкие, незаметные":
                        if select_med_type_5 == 'Крем':
                            cream_indices = [1, 4, 7, 10, 11]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [0, 3, 6, 9, 12]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [1, 4, 7, 10, 11]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Тоник':
                            toner_indices = [0, 3, 6, 9, 12]
                            selected_items = [tonic[i] for i in toner_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [1, 3, 5, 8, 10]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [0, 2, 5, 8, 11]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_indices = [1, 4, 7, 10, 11]
                            selected_items = [micellar_water[i] for i in micellar_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [0, 2, 5, 8, 11]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            gel_indices = [1, 3, 6, 9, 10]
                            selected_items = [Washing_gel[i] for i in gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))

                    elif select_tool_2 == "Расширенные":
                        if select_med_type_5 == 'Крем':
                            cream_indices = [0, 2, 5, 8, 11]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [1, 4, 7, 10, 12]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [0, 3, 6, 9, 11]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Тоник':
                            toner_indices = [1, 3, 6, 9, 12]
                            selected_items = [tonic[i] for i in toner_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [0, 2, 5, 8, 10]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [1, 4, 7, 10, 11]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_indices = [0, 5, 8, 11]
                            selected_items = [micellar_water[i] for i in micellar_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [3, 6, 9, 12]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            gel_indices = [7, 3, 6, 9]
                            selected_items = [Washing_gel[i] for i in gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))

                elif select_type_3 == "Нормальная":
                    if select_tool_2 == "Узкие, незаметные":
                        if select_med_type_5 == 'Крем':
                            cream_indices = [1, 3, 6, 9, 11]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [0, 2, 5, 8, 10]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [1, 4, 7, 10, 11]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Тоник':
                            toner_indices = [0, 3, 6, 9, 12]
                            selected_items = [tonic[i] for i in toner_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [1, 3, 5, 8, 10]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [0, 2, 5, 8, 11]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_indices = [1, 4, 7, 10, 11]
                            selected_items = [micellar_water[i] for i in micellar_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [0, 3, 6, 9, 11]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            gel_indices = [1, 4, 7, 10, 12]
                            selected_items = [Washing_gel[i] for i in gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))

                    elif select_tool_2 == "Расширенные":
                        if select_med_type_5 == 'Крем':
                            cream_indices = [17, 15]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [1, 3, 6, 12]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [2, 1, 5, 8, 11]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Тоник':
                            toner_indices = [1, 3, 6, 9, 12]
                            selected_items = [tonic[i] for i in toner_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [0, 2, 5, 8, 10]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [1, 4, 7, 10, 11]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_indices = [0, 3, 6, 9, 11]
                            selected_items = [micellar_water[i] for i in micellar_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [1, 4, 7, 10, 11]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            gel_indices = [0, 3, 6, 9, 10]
                            selected_items = [Washing_gel[i] for i in gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))

                elif select_type_3 == "Чувствительная":
                    if select_tool_2 == "Узкие, незаметные":
                        if select_med_type_5 == 'Крем':
                            cream_indices = [1, 3, 6, 9, 12]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [0, 2, 5, 8, 10]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [1, 4, 7, 10, 11]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Тоник':
                            toner_indices = [0, 3, 6, 9, 12]
                            selected_items = [tonic[i] for i in toner_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [1, 3, 5, 8, 10]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [0, 2, 5, 8, 11]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_indices = [1, 4, 7, 10, 11]
                            selected_items = [micellar_water[i] for i in micellar_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [0, 3, 6, 9, 11]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            gel_indices = [1, 4, 7, 10, 12]
                            selected_items = [Washing_gel[i] for i in gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))

                    elif select_tool_2 == "Расширенные":
                        if select_med_type_5 == 'Крем':
                            cream_indices = [0, 3, 6, 9, 11]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [1, 4, 7, 10, 12]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [0, 3, 6, 8, 11]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Тоник':
                            toner_indices = [1, 3, 6, 9, 12]
                            selected_items = [tonic[i] for i in toner_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [0, 2, 5, 8, 10]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [1, 4, 7, 10, 11]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_indices = [0, 2, 5, 8, 11]
                            selected_items = [micellar_water[i] for i in micellar_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [1, 3, 6, 9, 12]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            gel_indices = [0, 3, 6, 9, 10]
                            selected_items = [Washing_gel[i] for i in gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))

                elif select_type_3 == "Комбинированная":
                    if select_tool_2 == "Узкие, незаметные":
                        if select_med_type_5 == 'Крем':
                            cream_indices = [1, 4, 7, 10, 11]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [0, 2, 5, 8, 10]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [1, 4, 7, 10, 11]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Тоник':
                            toner_indices = [0, 3, 6, 9, 12]
                            selected_items = [tonic[i] for i in toner_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [1, 3, 5, 8, 10]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [0, 2, 5, 8, 11]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_indices = [1, 4, 7, 10, 11]
                            selected_items = [micellar_water[i] for i in micellar_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [0, 3, 6, 9, 11]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            gel_indices = [1, 4, 7, 10, 12]
                            selected_items = [Washing_gel[i] for i in gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))

                    elif select_tool_2 == "Расширенные":
                        if select_med_type_5 == 'Крем':
                            cream_indices = [0, 2, 5, 8, 11]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [1, 3, 6, 9, 12]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [0, 2, 5, 8, 11]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Тоник':
                            toner_indices = [1, 3, 6, 9, 12]
                            selected_items = [tonic[i] for i in toner_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [0, 2, 5, 8, 10]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [1, 4, 7, 10, 11]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_indices = [0, 3, 6, 9, 11]
                            selected_items = [micellar_water[i] for i in micellar_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [1, 4, 7, 10, 11]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            gel_indices = [0, 3, 6, 9, 10]
                            selected_items = [Washing_gel[i] for i in gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))

            elif select_score_1 == 'Чувствительность':
                if select_type_3 == "Сухая":
                    if select_tool_2 == "Аллергические реакции":
                        if select_med_type_5 == 'Крем':
                            cream_indices = [1, 3, 5, 8]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [0, 2, 4, 7]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [1, 3, 5, 8]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Тоник':
                            toner_indices = [0, 2, 4, 7]
                            selected_items = [tonic[i] for i in toner_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [1, 3, 5, 8]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [0, 2, 4, 7]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_indices = [1, 3, 5, 8]
                            selected_items = [micellar_water[i] for i in micellar_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [0, 2, 4, 7]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            gel_indices = [1, 3, 5, 8]
                            selected_items = [Washing_gel[i] for i in gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))

                    elif select_tool_2 == "Кожа реагирует на холодный воздух, сухой воздух":
                        if select_med_type_5 == 'Крем':
                            cream_indices = [0, 2, 4, 6]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [1, 3, 5, 7]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [0, 2, 4, 6]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Тоник':
                            toner_indices = [1, 3, 5, 7]
                            selected_items = [tonic[i] for i in toner_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [0, 2, 4, 6]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [1, 3, 5, 7]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_indices = [0, 2, 4, 6]
                            selected_items = [micellar_water[i] for i in micellar_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [1, 3, 5, 7]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            gel_indices = [0, 2, 4, 6]
                            selected_items = [Washing_gel[i] for i in gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))

                elif select_type_3 == "Жирная":
                    if select_tool_2 == "Аллергические реакции":
                        if select_med_type_5 == 'Крем':
                            cream_indices = [1, 3, 5, 7]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [0, 2, 4, 6]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [1, 3, 5, 7]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Тоник':
                            toner_indices = [0, 2, 4, 6]
                            selected_items = [tonic[i] for i in toner_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [1, 3, 5, 7]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [0, 2, 4, 6]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_indices = [1, 3, 5, 7]
                            selected_items = [micellar_water[i] for i in micellar_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [0, 2, 4, 6]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            gel_indices = [1, 3, 5, 7]
                            selected_items = [Washing_gel[i] for i in gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))

                    elif select_tool_2 == "Кожа реагирует на холодный воздух, сухой воздух":
                        if select_med_type_5 == 'Крем':
                            cream_indices = [0, 2, 5, 8]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [1, 3, 6, 9]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [0, 2, 5, 8]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Тоник':
                            toner_indices = [1, 3, 6, 9]
                            selected_items = [tonic[i] for i in toner_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [0, 2, 5, 8]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [1, 3, 6, 9]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_indices = [0, 2, 5, 8]
                            selected_items = [micellar_water[i] for i in micellar_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [1, 3, 6, 9]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            gel_indices = [0, 2, 5, 8]
                            selected_items = [Washing_gel[i] for i in gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))

                elif select_type_3 == "Нормальная":
                    if select_tool_2 == "Аллергические реакции":
                        if select_med_type_5 == 'Крем':
                            cream_indices = [1, 3, 5, 7]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [0, 2, 4, 6]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [1, 3, 5, 7]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Тоник':
                            toner_indices = [0, 2, 4, 6]
                            selected_items = [tonic[i] for i in toner_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [1, 3, 5, 7]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [0, 2, 4, 6]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_indices = [1, 3, 5, 7]
                            selected_items = [micellar_water[i] for i in micellar_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [0, 2, 4, 6]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            gel_indices = [1, 3, 5, 7]
                            selected_items = [Washing_gel[i] for i in gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))

                    elif select_tool_2 == "Кожа реагирует на холодный воздух, сухой воздух":
                        if select_med_type_5 == 'Крем':
                            cream_indices = [0, 2, 5, 8]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [1, 3, 6, 9]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [0, 2, 5, 8]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Тоник':
                            toner_indices = [1, 3, 6, 9]
                            selected_items = [tonic[i] for i in toner_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [0, 2, 5, 8]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [1, 3, 6, 9]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_indices = [0, 2, 5, 8]
                            selected_items = [micellar_water[i] for i in micellar_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [1, 3, 6, 9]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            gel_indices = [0, 2, 5, 8]
                            selected_items = [Washing_gel[i] for i in gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))

                elif select_type_3 == "Чувствительная":
                    if select_tool_2 == "Аллергические реакции":
                        if select_med_type_5 == 'Крем':
                            cream_indices = [1, 3, 5, 7]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [0, 2, 4, 6]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [1, 3, 5, 7]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Тоник':
                            toner_indices = [0, 2, 4, 6]
                            selected_items = [tonic[i] for i in toner_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [1, 3, 5, 7]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [0, 2, 4, 6]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_indices = [1, 3, 5, 7]
                            selected_items = [micellar_water[i] for i in micellar_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [0, 2, 4, 6]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            gel_indices = [1, 3, 5, 7]
                            selected_items = [Washing_gel[i] for i in gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))

                    elif select_tool_2 == "Кожа реагирует на холодный воздух, сухой воздух":
                        if select_med_type_5 == 'Крем':
                            cream_indices = [0, 2, 5, 8]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [1, 3, 6, 9]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [0, 2, 5, 8]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Тоник':
                            toner_indices = [1, 3, 6, 9]
                            selected_items = [tonic[i] for i in toner_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [0, 2, 5, 8]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [1, 3, 6, 9]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_indices = [0, 2, 5, 8]
                            selected_items = [micellar_water[i] for i in micellar_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [1, 3, 6, 9]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            gel_indices = [0, 2, 5, 8]
                            selected_items = [Washing_gel[i] for i in gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))

                elif select_type_3 == "Комбинированная":
                    if select_tool_2 == "Аллергические реакции":
                        if select_med_type_5 == 'Крем':
                            cream_indices = [1, 4, 7, 10]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [0, 3, 6, 9]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [1, 4, 7, 10]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Тоник':
                            toner_indices = [0, 3, 6, 9]
                            selected_items = [tonic[i] for i in toner_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [1, 4, 7, 10]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [0, 3, 6, 9, 1]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_indices = [1, 4, 7, 10]
                            selected_items = [micellar_water[i] for i in micellar_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [0, 3, 6, 9, 10]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            gel_indices = [1, 4, 7, 10, 11]
                            selected_items = [Washing_gel[i] for i in gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))

                    elif select_tool_2 == "Кожа реагирует на холодный воздух, сухой воздух":
                        if select_med_type_5 == 'Крем':
                            cream_indices = [0, 2, 4, 6]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [1, 3, 5, 7]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [0, 2, 4, 6]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Тоник':
                            toner_indices = [1, 3, 5, 7]
                            selected_items = [tonic[i] for i in toner_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [0, 2, 4, 6]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [1, 3, 5, 7]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_indices = [0, 2, 4, 6]
                            selected_items = [micellar_water[i] for i in micellar_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [1, 3, 5, 7]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            gel_indices = [0, 2, 4, 6]
                            selected_items = [Washing_gel[i] for i in gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))

            elif select_score_1 == 'Тон кожи':
                if select_type_3 == "Сухая":
                    if select_tool_2 == "Серый, тусклый":
                        if select_med_type_5 == 'Крем':
                            cream_indices = [1, 4, 7, 10]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [0, 3, 6, 9]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [1, 4, 7, 10]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Тоник':
                            toner_indices = [0, 3, 6, 9]
                            selected_items = [tonic[i] for i in toner_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [1, 4, 7, 10]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [0, 3, 6, 9]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_indices = [1, 4, 7, 10]
                            selected_items = [micellar_water[i] for i in micellar_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [0, 3, 6, 9]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            gel_indices = [1, 4, 7, 10]
                            selected_items = [Washing_gel[i] for i in gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))

                    elif select_tool_2 == "Здоровый, однородный":
                        if select_med_type_5 == 'Крем':
                            cream_indices = [0, 3, 6, 9]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [1, 4, 7, 10]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [0, 3, 6, 9]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Тоник':
                            toner_indices = [1, 4, 7, 10]
                            selected_items = [tonic[i] for i in toner_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [0, 3, 6, 9]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [1, 4, 7, 10]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_indices = [0, 3, 6, 9]
                            selected_items = [micellar_water[i] for i in micellar_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [1, 4, 7, 10]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            gel_indices = [0, 3, 6, 9]
                            selected_items = [Washing_gel[i] for i in gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))

                elif select_type_3 == "Жирная":
                    if select_tool_2 == "Серый, тусклый":
                        if select_med_type_5 == 'Крем':
                            cream_indices = [1, 4, 7, 10]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [0, 3, 6, 9]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [1, 4, 7, 10]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Тоник':
                            toner_indices = [0, 3, 6, 9]
                            selected_items = [tonic[i] for i in toner_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [1, 4, 7, 10]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [0, 3, 6, 9]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_indices = [1, 4, 7, 10]
                            selected_items = [micellar_water[i] for i in micellar_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [0, 3, 6, 9]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            gel_indices = [1, 4, 7, 10]
                            selected_items = [Washing_gel[i] for i in gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))

                    elif select_tool_2 == "Здоровый, однородный":
                        if select_med_type_5 == 'Крем':
                            cream_indices = [0, 3, 6, 9]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [1, 4, 7, 10]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [0, 3, 6, 9]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Тоник':
                            toner_indices = [1, 4, 7, 10]
                            selected_items = [tonic[i] for i in toner_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [0, 3, 6, 9]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [1, 4, 7, 10]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_indices = [0, 3, 6, 9]
                            selected_items = [micellar_water[i] for i in micellar_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [1, 4, 7, 10]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            gel_indices = [0, 3, 6, 9]
                            selected_items = [Washing_gel[i] for i in gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))

                elif select_type_3 == "Нормальная":
                    if select_tool_2 == "Серый, тусклый":
                        if select_med_type_5 == 'Крем':
                            cream_indices = [1, 4, 7, 10]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [0, 3, 6, 9]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [1, 4, 7, 10]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Тоник':
                            toner_indices = [0, 3, 6, 9]
                            selected_items = [tonic[i] for i in toner_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [1, 4, 7, 10]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [0, 3, 6, 9]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_indices = [1, 4, 7, 10]
                            selected_items = [micellar_water[i] for i in micellar_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [0, 3, 6, 9]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            gel_indices = [1, 4, 7, 10]
                            selected_items = [Washing_gel[i] for i in gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))

                    elif select_tool_2 == "Здоровый, однородный":
                        if select_med_type_5 == 'Крем':
                            cream_indices = [0, 3, 6, 9]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [1, 4, 7, 10]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [0, 3, 6, 9]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Тоник':
                            toner_indices = [1, 4, 7, 10]
                            selected_items = [tonic[i] for i in toner_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [0, 3, 6, 9]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [1, 4, 7, 10]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_indices = [0, 3, 6, 9]
                            selected_items = [micellar_water[i] for i in micellar_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [1, 4, 7, 10]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            gel_indices = [0, 3, 6, 9]
                            selected_items = [Washing_gel[i] for i in gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))

                elif select_type_3 == "Чувствительная":
                    if select_tool_2 == "Серый, тусклый":
                        if select_med_type_5 == 'Крем':
                            cream_indices = [1, 3, 6, 8]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [0, 3, 6, 9]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [1, 4, 7, 10]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Тоник':
                            toner_indices = [0, 3, 6, 9]
                            selected_items = [tonic[i] for i in toner_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [1, 4, 7, 10]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [0, 3, 6, 9]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_indices = [1, 4, 7, 10]
                            selected_items = [micellar_water[i] for i in micellar_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [0, 3, 6, 9]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            gel_indices = [1, 4, 7, 10]
                            selected_items = [Washing_gel[i] for i in gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))

                    elif select_tool_2 == "Здоровый, однородный":
                        if select_med_type_5 == 'Крем':
                            cream_indices = [0, 3, 6, 9]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [1, 4, 7, 10]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [0, 3, 6, 9]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Тоник':
                            toner_indices = [1, 4, 7, 10]
                            selected_items = [tonic[i] for i in toner_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [0, 3, 6, 9]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [1, 4, 7, 10]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_indices = [0, 3, 6, 9]
                            selected_items = [micellar_water[i] for i in micellar_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [1, 4, 7, 10]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            gel_indices = [0, 3, 6, 9]
                            selected_items = [Washing_gel[i] for i in gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))

                elif select_type_3 == "Комбинированная":
                    if select_tool_2 == "Серый, тусклый":
                        if select_med_type_5 == 'Крем':
                            cream_indices = [1, 3, 6, 8]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [0, 3, 6, 9]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [1, 4, 7, 10]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Тоник':
                            toner_indices = [0, 3, 6, 9]
                            selected_items = [tonic[i] for i in toner_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [1, 4, 7, 10]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [0, 3, 6, 9]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_indices = [1, 4, 7, 10]
                            selected_items = [micellar_water[i] for i in micellar_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [0, 3, 6, 9]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            gel_indices = [1, 4, 7, 10]
                            selected_items = [Washing_gel[i] for i in gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))

                    elif select_tool_2 == "Здоровый, однородный":
                        if select_med_type_5 == 'Крем':
                            cream_indices = [0, 2, 5, 7]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [1, 4, 6, 9]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [0, 3, 6, 9]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Тоник':
                            toner_indices = [1, 4, 7, 10]
                            selected_items = [tonic[i] for i in toner_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [0, 2, 5, 7]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [1, 3, 6, 9]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_indices = [0, 2, 5, 7]
                            selected_items = [micellar_water[i] for i in micellar_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [1, 4, 7, 10]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            gel_indices = [0, 3, 6, 9]
                            selected_items = [Washing_gel[i] for i in gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))

            elif select_score_1 == 'Морщины':
                if select_type_3 == "Сухая":
                    if select_tool_2 == "Возрастные":
                        if select_med_type_5 == 'Крем':
                            cream_indices = [0, 1, 2, 3, 4, 5]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [6, 7, 8, 9, 10, 11]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [1, 9, 7, 3, 12]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Тоник':
                            toner_indices = [10, 5, 2, 8, 11, 15]
                            selected_items = [tonic[i] for i in toner_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [4, 6, 13, 0, 7, 2]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [11, 8, 5, 6, 3, 14]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_indices = [9, 4, 10, 0, 12, 15]
                            selected_items = [micellar_water[i] for i in micellar_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [7, 13, 1, 2, 6, 11]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            gel_indices = [0, 4, 9, 12, 15, 5]
                            selected_items = [Washing_gel[i] for i in gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                    elif select_tool_2 == "Отсутствуют":
                        if select_med_type_5 == 'Крем':
                            cream_indices = [10, 13, 8, 3, 1, 14]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [2, 11, 6, 7, 5, 12]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [0, 4, 9, 10, 8]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Тоник':
                            toner_indices = [3, 13, 1, 14, 2]
                            selected_items = [tonic[i] for i in toner_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [9, 10, 3, 0, 2, 4]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [6, 13, 14, 7, 12, 1]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_indices = [8, 11, 15, 5, 9, 10]
                            selected_items = [micellar_water[i] for i in micellar_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [2, 3, 0, 4, 6, 13]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            gel_indices = [1, 7, 12, 8, 14, 11]
                            selected_items = [Washing_gel[i] for i in gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                elif select_type_3 == "Жирная":
                    if select_tool_2 == "Возрастные":
                        if select_med_type_5 == 'Крем':
                            cream_indices = [10, 5, 9, 6, 15, 3]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [2, 13, 4, 0, 7, 12]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [11, 1, 8, 10, 5]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Тоник':
                            toner_indices = [15, 3, 9, 6, 2, 4]
                            selected_items = [tonic[i] for i in toner_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [7, 13, 12, 0, 11, 8]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [1, 10, 14, 5, 4, 15]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_indices = [9, 2, 6, 3, 7, 11]
                            selected_items = [micellar_water[i] for i in micellar_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [8, 0, 12, 1, 10, 13]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            gel_indices = [15, 4, 5, 9, 11, 6]
                            selected_items = [Washing_gel[i] for i in gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                    elif select_tool_2 == "Отсутствуют":
                        if select_med_type_5 == 'Крем':
                            cream_indices = [7, 3, 14, 2, 8, 13]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [1, 10, 5, 2, 7, 9]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [12, 8, 3, 11, 6]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Тоник':
                            toner_indices = [13, 0, 4, 15, 2, 7]
                            selected_items = [tonic[i] for i in toner_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [9, 5, 12, 3, 10, 1]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [8, 6, 15, 13, 11, 4]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_indices = [2, 14, 0, 7, 10, 9]
                            selected_items = [micellar_water[i] for i in micellar_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [3, 5, 11, 12, 1, 8]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            gel_indices = [0, 3, 6, 9]
                            selected_items = [Washing_gel[i] for i in gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                elif select_type_3 == "Нормальная":
                    if select_tool_2 == "Возрастные":
                        if select_med_type_5 == 'Крем':
                            cream_indices = [6, 13, 4, 15, 2, 7]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [10, 9, 14, 0, 1, 12]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [5, 11, 8, 6, 3]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Тоник':
                            toner_indices = [2, 13, 4, 10, 7, 1]
                            selected_items = [tonic[i] for i in toner_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [14, 9, 12, 0, 11, 3]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [8, 6, 15, 2, 5, 13]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_indices = [4, 7, 10, 1, 14, 9]
                            selected_items = [micellar_water[i] for i in micellar_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [12, 3, 11, 8, 0, 6]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            gel_indices = [15, 2, 5, 13, 9, 4]
                            selected_items = [Washing_gel[i] for i in gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                    elif select_tool_2 == "Отсутствуют":
                        if select_med_type_5 == 'Крем':
                            cream_indices = [8, 11, 6, 14, 9, 4]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [3, 9, 0, 14, 12, 4]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [11, 4, 6, 5, 2]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Тоник':
                            toner_indices = [8, 12, 14, 1, 9, 0]
                            selected_items = [tonic[i] for i in toner_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [10, 3, 13, 7, 2, 6]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [7, 5, 9, 13, 2, 11]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_indices = [15, 3, 12, 8, 0, 14]
                            selected_items = [micellar_water[i] for i in micellar_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [2, 10, 13, 6, 4, 11]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            gel_indices = [9, 5, 7, 1, 14, 0]
                            selected_items = [Washing_gel[i] for i in gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                elif select_type_3 == "Чувствительная":
                    if select_tool_2 == "Возрастные":
                        if select_med_type_5 == 'Крем':
                            cream_indices = [6, 12, 15, 3, 11, 8]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [3, 9, 4, 12, 15, 7]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [5, 6, 10, 12, 0, 8]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Тоник':
                            toner_indices = [11, 14, 1, 9, 7, 0]
                            selected_items = [tonic[i] for i in toner_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [4, 3, 13, 10, 5, 9]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [12, 1, 15, 6, 9, 2]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_indices = [14, 3, 8, 10, 6, 5]
                            selected_items = [micellar_water[i] for i in micellar_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [9, 7, 15, 1, 11, 0]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            gel_indices = [7, 5, 1, 2, 3, 8]
                            selected_items = [Washing_gel[i] for i in gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                    elif select_tool_2 == "Отсутствуют":
                        if select_med_type_5 == 'Крем':
                            cream_indices = [15, 14, 4, 0, 7, 11]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [2, 6, 5, 8, 13, 12]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [1, 3, 0, 2, 6, 10]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Тоник':
                            toner_indices = [2, 6, 5, 8, 13, 12]
                            selected_items = [tonic[i] for i in toner_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [15, 14, 4, 0, 7, 11]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [2, 6, 5, 8, 13, 12]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_indices = [1, 3, 0, 2, 6, 10]
                            selected_items = [micellar_water[i] for i in micellar_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [14, 5, 3, 6, 9, 12]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            gel_indices = [4, 8, 15, 7, 14, 10]
                            selected_items = [Washing_gel[i] for i in gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                elif select_type_3 == "Комбинированная":
                    if select_tool_2 == "Возрастные":
                        if select_med_type_5 == 'Крем':
                            cream_indices = [1, 5, 9, 2, 12, 10]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [6, 0, 15, 8, 13, 3]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [11, 7, 4, 12, 2, 10]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Тоник':
                            toner_indices = [9, 13, 5, 1, 0, 12]
                            selected_items = [tonic[i] for i in toner_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [15, 8, 3, 10, 14, 9]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [7, 11, 2, 6, 12, 4]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_indices = [13, 15, 0, 3, 7, 1]
                            selected_items = [micellar_water[i] for i in micellar_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [5, 8, 9, 14, 4, 11]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            gel_indices = [2, 10, 12, 6, 1, 3]
                            selected_items = [Washing_gel[i] for i in gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                    elif select_tool_2 == "Отсутствуют":
                        if select_med_type_5 == 'Крем':
                            cream_indices = [7, 4, 14, 11, 10, 8]
                            selected_items = [cream[i] for i in cream_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Сыворотка':
                            serum_indices = [9, 5, 1, 2, 15, 6]
                            selected_items = [serum[i] for i in serum_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Лосьон':
                            lotion_indices = [3, 10, 0, 12, 8, 11]
                            selected_items = [lotion[i] for i in lotion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Тоник':
                            toner_indices = [10, 15, 4, 6, 7, 11]
                            selected_items = [tonic[i] for i in toner_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Маска':
                            mask_indices = [1, 9, 2, 5, 13, 12]
                            selected_items = [mask[i] for i in mask_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Скраб':
                            scrub_indices = [0, 8, 3, 10, 7, 14]
                            selected_items = [scrub[i] for i in scrub_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Мицеллярная вода':
                            micellar_indices = [11, 4, 6, 2, 15, 9]
                            selected_items = [micellar_water[i] for i in micellar_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Эмульсия':
                            emulsion_indices = [4, 10, 1, 14, 9, 3]
                            selected_items = [emulsion[i] for i in emulsion_indices]
                            label_otvet = QLabel('\n'.join(selected_items))
                        elif select_med_type_5 == 'Гель для умывания':
                            gel_indices = [2, 5, 6, 8, 13, 12]
                            selected_items = [Washing_gel[i] for i in gel_indices]
                            label_otvet = QLabel('\n'.join(selected_items))

            opredelenie_type = combo_box_3.currentText()

            if opredelenie_type == "Комбинированная":
                label = QLabel(
                    f"Исходя из предоставленных параметров и характеристик кожи, можно сделать следующие выводы по типу кожи: '{self.spisok_result_tovar[2]}'. \n"
                    f"Данная кожа относится к комбинированному типу. Это означает, что на разных участках лица могут проявляться различные особенности, \n\n"
                    f"Такие как умеренное выделение масла в области лба, носа и подбородка, в то время как другие участки могут быть более сухими.\n"

                    f"Такой тип кожи требует балансировки ухода, учитывая особенности как жирных, так и сухих участков. \n\n"
                    f"Это свидетельствует о необходимом лечении, для Вас необходимо: {self.spisok_result_tovar[3].lower()}. \n"
                    f"Данную процедуру Вы будете проводить следующим типом продукции: {self.spisok_result_tovar[4].lower()}. \n\n"
                    f"Чтобы обеспечить комплексное и эффективное увлажнение, очищение и поддержание здоровья кожного "
                    f"покрова.\n"
                    f"Регулярный уход за комбинированной кожей поможет достичь баланса, свойственных обоим типам кожи, и сохранить ее здоровье и сияние."
                )
                label_dopol = QLabel(
                    f"Эти продукты обеспечивают всесторонний уход, идеально подходящий для комбинированной кожи. \n"
                    f"Помогая ей сохранить здоровье и естественную красоту. Независимо от того, имеются ли у вас участки с избытком масла или более сухие области.\n "
                    f"Эти средства способны обеспечить увлажнение, питание и поддержание необходимого баланса для достижения оптимального состояния кожи. \n"
                    f"Выберите эти продукты, чтобы обеспечить заботливый уход и поддерживать здоровье вашей комбинированной кожи, достигая ее сияющего и ухоженного вида.\n"
                    f"Эти средства помогут, так как Вам требуется уход и {self.spisok_result_tovar[3].lower()}.\n")
            else:
                label = QLabel(
                    f"Исходя из предоставленных параметров и характеристик кожи, можно сделать следующие выводы по типу кожи: '{self.spisok_result_tovar[2].lower()}'\n"
                    f"Ваше состояние проявляет: {self.spisok_result_tovar[0].lower()}, и выделяет: {self.spisok_result_tovar[1].lower()}.\n\n"
                    f"Это свидетельствует о необходимом лечении, для Вас необходимо: {self.spisok_result_tovar[3].lower()}. \n"
                    f"Данную процедуру Вы будете проводить следующим типом продукции: {self.spisok_result_tovar[4].lower()}. "
                    f"Ваша кожа требует ухода и {self.spisok_result_tovar[3].lower()}.\n\n"
                    f"Все товары выбраны исключительно по Вашим параметрам и характеристках, а также целью ухода: {self.spisok_result_tovar[5].lower()}\n"
                    f"Отталкиваясь от всех параметров кожи, можно сделать следующий список рекомендованных продуктов для Вас:")

                label_dopol = QLabel(
                    f"Эти продукты предоставляют всесторонний уход для вашей кожи, помогая сохранить её здоровье и красоту. \n"
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
