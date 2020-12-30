from collections import OrderedDict

from .. import Provider as PersonProvider


class Provider(PersonProvider):
    formats_female = OrderedDict((
        ('{{first_name_female}} {{last_name}}', 0.9),
        ('{{prefix_female}} {{first_name_female}} {{last_name}}', 0.1),
    ))

    formats_male = OrderedDict((
        ('{{first_name_male}} {{last_name}}', 0.9),
        ('{{prefix_male}} {{first_name_male}} {{last_name}}', 0.1),
    ))

    formats = formats_female.copy()
    formats.update(formats_male)

    # Source: uk.wikipedia.org/wiki/Українські_імена
    first_names_male = (
        'Аарон', 'Августин', 'Аврелій', 'Адам', 'Азар', 'Алевтин', 'Альберт',
        'Амвросій', 'Андрій', 'Антон', 'Аркадій', 'Арсен', 'Артем', 'Орхип',
        'Богдан', 'Богодар', 'Богуслав', 'Болеслав', 'Борис', 'Борислав',
        'Вадим', 'Валентин', 'Валерій', 'Варфоломій', 'Василь', 'Венедикт',
        'Веніямин', 'Віктор', 'Віталій', 'Владислав', 'Володимир',
        'Вʼячеслав', 'Гаврило', 'Геннадій', 'Георгій', 'Герман ', 'Гордій',
        'Григорій', 'Гліб', 'Данило', 'Давид', 'Дан', 'Демид', 'Демʼян',
        'Дмитро', 'Захар', 'Зиновій', 'Зорян', 'Іван', 'Ігнат', 'Ігор', 'Ілля',
        'Едуард', 'Євген', 'Єлисей', 'Єфрем', 'Йосип', 'Климент', 'Костянтин',
        'Левко', 'Лесь', 'Леон', 'Леонід', 'Леонтій', 'Леопольд', 'Лукʼян',
        'Кирило', 'Макар', 'Максим', 'Марко', 'Мартин', 'Микита', 'Миколай',
        'Мирон', 'Мирослав', 'Михайло', 'Назар', 'Нестор', 'Олег', 'Олекса',
        'Олександр', 'Олесь', 'Омелян', 'Онисим', 'Опанас', 'Орест', 'Остап',
        'Охрім', 'Петро', 'Павло', 'Панас', 'Пантелеймон', 'Пармен', 'Пилип',
        'Прохір', 'Роман', 'Ростислав', 'Руслан', 'Святослав', 'Семен',
        'Сергій', 'Симон', 'Соломон', 'Спас', 'Станіслав', 'Степан', 'Стефан',
        'Тарас', 'Теодор', 'Тимофій', 'Трохим', 'Устим', 'Федір', 'Феофан',
        'Франц', 'Хома', 'Юстим', 'Юхим', 'Яків', 'Ярема', 'Ярослав',
    )

    first_names_female = (
        'Ада', 'Аліна', 'Алла', 'Альбіна', 'Амалія', 'Анастасія', 'Аніта',
        'Анжела', 'Ганна', 'Богуслава', 'Богданна', 'Валентина', 'Варвара',
        'Василина', 'Вікторія', 'Віолетта', 'Віра', 'Володимира', 'Галина',
        'Данна', 'Дарина', 'Едита', 'Єва', 'Єлисавета', 'Емілія', 'Еріка',
        'Ірина', 'Ірена', 'Златослава', 'Камілла', 'Клавдія', 'Лариса', 'Ліза',
        'Лілія', 'Людмила', 'Любов', 'Марія', 'Марина', 'Марта', 'Марʼяна',
        'Маруся', 'Михайлина', 'Мілена', 'Надія', 'Наталія', 'Пріска',
        'Розалія', 'Святослава', 'Сніжана', 'Соломія', 'Софія', 'Одарка',
        'Оксана', 'Оксенія', 'Олена', 'Ольга', 'Орина', 'Орися', 'Роксолана',
        'Світлана', 'Тереза', 'Тетяна', 'Юстина', 'Христина', 'Ярина',
        'Ярослава',
    )

    first_names = first_names_male + first_names_female

    # Source: uk.wikipedia.org/wiki/Категорія:Українські_прізвища
    last_names = (
        'Абрагамовський', 'Абраменко', 'Абрамчук', 'Авдєєнко', 'Аверченко',
        'Авраменко', 'Аврамчук', 'Адаменко', 'Адамчук', 'Ажажа', 'Акименко',
        'Акуленко', 'Александренко', 'Алексеєнко', 'Алексійчук', 'Алексюк',
        'Андрейко', 'Андрієвич', 'Андрієнко', 'Андріїшин', 'Андрійович',
        'Андрійчук', 'Андрощук', 'Андрусенко', 'Аронець', 'Арсенич',
        'Артеменко', 'Артим', 'Артимишин', 'Артимович', 'Артюх', 'Артюшенко',
        'Архимович', 'Архипенко', 'Асаула', 'Атаманчук', 'Атаманюк',
        'Атрощенко', 'Бабʼюк', 'Бабʼяк', 'Бабак', 'Бабариченко', 'Бабенко',
        'Бабич', 'Бабиченко', 'Бабій', 'Бабійчук', 'Бабко', 'Базавлученко',
        'Базилевич', 'Базилевський', 'Байда', 'Байдак', 'Байрак', 'Баклан',
        'Бакуменко', 'Балабан', 'Бандера', 'Бандура', 'Бандурка', 'Барабаш',
        'Баран', 'Баранець', 'Бараник', 'Баранник', 'Батіг', 'Батуринець',
        'Батюк', 'Башполченко', 'Баштан', 'Бгиденко', 'Бебешко', 'Бевз',
        'Бевзенко', 'Безбородьки', 'Безбородько', 'Бездітко', 'Вакарчук',
        'Вакуленко', 'Валенко', 'Ванченко', 'Василашко', 'Василевич',
        'Василенко', 'Василечко', 'Ватаманюк', 'Вахній', 'Ващенко',
        'Ващенко-Захарченко', 'Ващук', 'Вдовенко', 'Вдовиченко', 'Величко',
        'Венгринович', 'Вергун', 'Верес', 'Верменич', 'Вернигора', 'Вернидуб',
        'Вертипорох', 'Верховинець', 'Верхола', 'Височан', 'Вишиваний',
        'Вишняк', 'Вівчаренко', 'Вітер', 'Вітрук', 'Власенко', 'Власюк',
        'Влох', 'Воблий', 'Вовк', 'Габелко', 'Гавриленко', 'Гаврилець',
        'Гаврилишин', 'Гаврилів', 'Гаврилюк', 'Гавриш', 'Гавришкевич',
        'Гаврюшенко', 'Гаєвський', 'Гайворонський', 'Гайда', 'Гайдабура',
        'Гайдай', 'Гайдамака', 'Гайденко', 'Гоголь', 'Гоголь-Яновський',
        'Годунок', 'Голик', 'Голобородько', 'Гресь', 'Гречаник', 'Гречко',
        'Гриценко', 'Гузенко', 'Гузій', 'Гузь', 'Гук', 'Гунько', 'Гупало',
        'Гуцуляк', 'Ґалаґан', 'Ґереґа', 'Ґерета', 'Ґерус', 'Ґжицький', 'Ґоляш',
        'Давиденко', 'Давимука', 'Даниленко', 'Данилюк', 'Данильчук',
        'Данченко', 'Данчук', 'Данькевич', 'Даньків', 'Данько', 'Дараган',
        'Дахно', 'Даценко', 'Дацюк', 'Дашенко', 'Дашкевич', 'Девдюк',
        'Дейнека', 'Дейнеко', 'Дейсун', 'Демʼяненко', 'Демʼянчук', 'Демʼянюк',
        'Демиденко', 'Дергач', 'Деревʼянко', 'Дерегус', 'Деркач', 'Деряжний',
        'Джунь', 'Джус', 'Дробʼязко', 'Дробаха', 'Дрозд', 'Дрозденко',
        'Дубас', 'Дубенко', 'Дубина', 'Дзиндра', 'Дзюба', 'Доценко', 'Дуплій',
        'Дурдинець', 'Дутка', 'Ейбоженко', 'Євдокименко', 'Євтушенко',
        'Євтушок', 'Ємельяненко', 'Ємець', 'Єременко', 'Єресько', 'Єрмоленко',
        'Єрошенко', 'Єрченко', 'Єрьоменко', 'Єсипенко', 'Єфименко', 'Єщенко',
        'Жадан', 'Жайворон', 'Жаліло', 'Жарко', 'Жук', 'Журавель', 'Журба',
        'Жученко', 'Забара', 'Забарний', 'Забашта', 'Забіла', 'Заєць', 'Заїка',
        'Зайченко', 'Закусило', 'Запорожець', 'Заруба', 'Зарудний', 'Засенко',
        'Засуха', 'Засядько', 'Затовканюк', 'Затула', 'Захаренко',
        'Захарченко', 'Зінкевич', 'Зінченко', 'Зінчук', 'Зубко', 'Іваненко',
        'Іваничук', 'Іванченко', 'Івасюк', 'Іващенко', 'Ільєнко', 'Ільченко',
        'Ірванець', 'Ісаєвич', 'Ісаєнко', 'Іщак', 'Іщенко', 'Їжак', 'Їжакевич',
        'Кабалюк', 'Кабаненко', 'Каденюк', 'Калениченко', 'Кальченко',
        'Канівець', 'Карась', 'Кармалюк', 'Карпа', 'Карпенко', 'Кащенко',
        'Кибкало', 'Килимник', 'Кириленко', 'Коваленко', 'Ковалюк', 'Ковпак',
        'Козак', 'Козаченко', 'Колесниченко', 'Колісниченко', 'Колодуб',
        'Комар', 'Конопленко', 'Конопля', 'Копитко', 'Корбут', 'Корж',
        'Короленко', 'Корпанюк', 'Корсун', 'Лаба', 'Лавренко', 'Лагода',
        'Лазаренко', 'Левченко', 'Лемешко', 'Лесик', 'Лисенко', 'Литвин',
        'Литвиненко', 'Лубенець', 'Лукаш', 'Лупій', 'Луценко', 'Ляшко',
        'Мазепа', 'Мазур', 'Макаренко', 'Макогон', 'Малик', 'Малишко',
        'Мамчур', 'Масляк', 'Масоха', 'Матвієнко', 'Матяш', 'Медведенко',
        'Микитюк', 'Михайличенко', 'Михайлюк', 'Михалюк', 'Мірошниченко',
        'Міщенко', 'Москаль', 'Назаренко', 'Наливайко', 'Негода', 'Непорожній',
        'Нестайко', 'Нестеренко', 'Ніколюк', 'Носаченко', 'Носенко',
        'Оберемко', 'Овсієнко', 'Овчаренко', 'Олійник', 'Оліфіренко',
        'Онищенко', 'Оніщук', 'Онуфрієнко', 'Опанасенко', 'Орлик', 'Оробець',
        'Остапчук', 'Охримович', 'Охріменко', 'Пʼятаченко', 'Павленко',
        'Павлик', 'Павличенко', 'Палій', 'Панчук', 'Парасюк', 'Пелех',
        'Перебийніс', 'Перепелиця', 'Петлюра', 'Петренко', 'Петрик',
        'Пилипенко', 'Піддубний', 'Полтавець', 'Приймак', 'Примаченко',
        'Притула', 'Приходько', 'Прокопович', 'Проценко', 'Пустовіт', 'Пушкар',
        'Радченко', 'Рак', 'Ребрик', 'Рева', 'Редько', 'Романенко', 'Романець',
        'Романчук', 'Рубан', 'Рубець', 'Рудик', 'Рудько', 'Рябець', 'Рябовіл',
        'Рябошапка', 'Рябченко', 'Савенко', 'Сагаль', 'Саєнко', 'Салій',
        'Самойленко', 'Сацюк', 'Саченко', 'Свириденко', 'Свистун',
        'Семенченко', 'Симоненко', 'Сиротенко', 'Сич', 'Сімашкевич', 'Сірко',
        'Сіробаба', 'Сірченко', 'Скиба', 'Скирда', 'Скопенко', 'Скорик',
        'Скоробогатько', 'Смик', 'Слюсар', 'Сомко', 'Стельмах', 'Стець',
        'Стус', 'Супруненко', 'Талан', 'Таран', 'Тарасенко', 'Твердохліб',
        'Теличенко', 'Теліженко', 'Терещенко', 'Терещук', 'Тесленко', 'Тесля',
        'Тимченко', 'Тимчук', 'Титаренко', 'Тихий', 'Тичина', 'Ткач',
        'Ткаченко', 'Товстоліс', 'Товстуха', 'Токар', 'Тригуб', 'Туркало',
        'Тягнибок', 'Удовенко', 'Удовиченко', 'Уманець', 'Усик', 'Устенко',
        'Фаренюк', 'Фартушняк', 'Фастенко', 'Фесенко', 'Філіпенко', 'Фоменко',
        'Франко', 'Франчук', 'Фурс', 'Харченко', 'Хмара', 'Хоменко', 'Хомик',
        'Хорішко', 'Христенко', 'Христич', 'Худобʼяк', 'Худяк', 'Царенко',
        'Цибуленко', 'Цимбал', 'Цимбалюк', 'Цісик', 'Цушко', 'Цюпа', 'Цюцюра',
        'Чабан', 'Чайка', 'Чаленко', 'Чалий', 'Чарниш', 'Чекалюк',
        'Червоненко', 'Чередник', 'Черінько', 'Черненко', 'Чміль', 'Чорновіл',
        'Чубай', 'Чуйко', 'Чумак', 'Чумаченко', 'Чуприна', 'Шаблій', 'Шамрай',
        'Шаповал', 'Шахрай', 'Швайка', 'Швачка', 'Швачко', 'Шведченко',
        'Шеремета', 'Шевченко', 'Шелест', 'Шеремет', 'Шило', 'Шинкаренко',
        'Шиян', 'Шморгун', 'Шовкопляс', 'Штепа', 'Штокало', 'Шутько',
        'Шухевич', 'Щербак', 'Щербань', 'Щириця', 'Щорс', 'Юрченко', 'Юрчишин',
        'Юрчук', 'Юхименко', 'Ющенко', 'Якименко', 'Якимчук', 'Яковенко',
        'Ярема', 'Яременко', 'Яремків', 'Яремко', 'Яремчук', 'Ярош', 'Яценко',
        'Яценюк', 'Ященко', 'Ящук',
    )

    prefixes_male = ('пан',)
    prefixes_female = ('пані',)
