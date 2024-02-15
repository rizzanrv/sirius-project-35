import config
import disnake
from disnake.ext import commands
import random

intents = disnake.Intents.all()
bot = commands.Bot(command_prefix='.', intents=intents)
bot.remove_command('help')

algebra_questions = [
    {
        "question": "Решите уравнение: 2x + 5 = 13",
        "options": ["4", "3", "2", "6"],
        "correct_option": "6"
    },
    {
        "question": "Упростите выражение: 3(x + 4) - 2(2x - 1)",
        "options": ["-5x + 14", "-3x + 10", "5x - 14", "3x - 10"],
        "correct_option": "-5x + 14"
    },
    {
        "question": "Найдите корень уравнения: x^2 - 9 = 0",
        "options": ["3", "-3", "2", "-2"],
        "correct_option": "3"
    },
    {
        "question": "Решите уравнение: 3x - 7 = 8",
        "options": ["5", "3", "2", "6"],
        "correct_option": "5"
    },
    {
        "question": "Упростите выражение: 5(x + 2) - (3x - 1)",
        "options": ["2x + 9", "-8x + 11", "-8x + 9", "-2x + 11"],
        "correct_option": "-8x + 11"
    },
    {
        "question": "Найдите корень уравнения: x^2 - 49 = 0",
        "options": ["7", "-7", "9", "-9"],
        "correct_option": "7"
    },
    {
        "question": "Решите уравнение: x - 8 = -12",
        "options": ["-4", "-6", "-20", "-16"],
        "correct_option": "-4"
    },
    {
        "question": "Упростите выражение: 4(x + 2) - 2(3x - 1)",
        "options": ["-7x + 10", "-5x + 8", "7x - 10", "5x - 8"],
        "correct_option": "-7x + 10"
    },
    {
        "question": "Найдите корень уравнения: x^2 - 16 = 0",
        "options": ["4", "-4", "2", "-2"],
        "correct_option": "4"
    },
    {
        "question": "Решите уравнение: 4x + 3 = 19",
        "options": ["4", "3", "2", "5"],
        "correct_option": "4"
    },
    {
        "question": "Упростите выражение: 2(x + 5) - 3(2x - 1)",
        "options": ["-7x + 11", "-5x + 7", "7x - 11", "5x - 7"],
        "correct_option": "-7x + 11"
    },
    {
        "question": "Найдите корень уравнения: x^2 - 25 = 0",
        "options": ["5", "-5", "4", "-4"],
        "correct_option": "5"
    },
    {
        "question": "Решите уравнение: 5x - 9 = 6",
        "options": ["3", "2", "1", "2/5"],
        "correct_option": "3"
    },
    {
        "question": "Упростите выражение: 3(x + 3) - 2(2x - 2)",
        "options": ["-7x + 7", "-5x + 1", "7x - 7", "5x - 1"],
        "correct_option": "-7x + 7"
    },
    {
        "question": "Найдите корень уравнения: x^2 - 36 = 0",
        "options": ["6", "-6", "5", "-5"],
        "correct_option": "6"
    }
]

geometry_questions = [
    {
        "question": "Найдите площадь прямоугольника со сторонами 5 и 8.",
        "options": ["40", "13", "26", "20"],
        "correct_option": "40"
    },
    {
        "question": "Чему равна длина гипотенузы прямоугольного треугольника со сторонами 3 и 4?",
        "options": ["5", "6", "7", "8"],
        "correct_option": "5"
    },
    {
        "question": "Найдите периметр круга с радиусом 10.",
        "options": ["20π", "30π", "40π", "50π"],
        "correct_option": "20π"
    },
    {
        "question": "Найдите площадь квадрата со стороной 12.",
        "options": ["144", "48", "36", "64"],
        "correct_option": "144"
    },
    {
        "question": "Чему равен объем прямоугольного параллелепипеда с длиной 6, шириной 4 и высотой 3?",
        "options": ["72", "48", "36", "24"],
        "correct_option": "72"
    },
    {
        "question": "Найдите длину окружности с радиусом 7.",
        "options": ["14π", "21π", "28π", "35π"],
        "correct_option": "14π"
    },
    {
        "question": "Найдите площадь треугольника со сторонами 9, 12 и 15.",
        "options": ["54", "36", "27", "45"],
        "correct_option": "54"
    },
    {
        "question": "Чему равен объем шара с радиусом 4?",
        "options": ["256π", "128π", "64π", "32π"],
        "correct_option": "256π"
    },
    {
        "question": "Найдите периметр прямоугольника со сторонами 10 и 15.",
        "options": ["40", "35", "25", "30"],
        "correct_option": "50"
    },
    {
        "question": "Найдите площадь круга с радиусом 5.",
        "options": ["25π", "50π", "75π", "100π"],
        "correct_option": "25π"
    },
    {
        "question": "Чему равен объем цилиндра с радиусом основания 3 и высотой 8?",
        "options": ["72π", "144π", "216π", "288π"],
        "correct_option": "72π"
    },
    {
        "question": "Найдите площадь треугольника со сторонами 4 и 6 и углом между ними 60 градусов.",
        "options": ["8", "12", "10", "6"],
        "correct_option": "12"
    },
    {
        "question": "Найдите периметр квадрата со стороной 7.",
        "options": ["21", "28", "35", "14"],
        "correct_option": "28"
    },
    {
        "question": "Найдите площадь круга с радиусом 10.",
        "options": ["100π", "50π", "200π", "25π"],
        "correct_option": "100π"
    },
    {
        "question": "Найдите объем прямоугольного параллелепипеда со сторонами 3, 4 и 5.",
        "options": ["60", "30", "40", "20"],
        "correct_option": "60"
    },
    {
        "question": "Найдите длину окружности с радиусом 12.",
        "options": ["24π", "12π", "48π", "36π"],
        "correct_option": "24π"
    }
]


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')


@bot.slash_command(name="start")
async def start(ctx):
    tasks = [algebra_task, geometry_task]
    total_correct = 0
    total_tasks = 15

    for i in range(total_tasks):
        task = random.choice(tasks)
        total_correct += await task(ctx, i + 1)

    await ctx.send(f"Итог: Вы правильно ответили на {total_correct} из {total_tasks} задач.")


async def algebra_task(ctx, task_number):
    question_data = random.choice(algebra_questions)
    correct_answer = question_data["correct_option"]

    await ctx.send(f"({task_number}) {question_data['question']}")
    await ctx.send(f"Варианты ответов: {question_data['options']}")

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel

    try:
        user_answer = await bot.wait_for("message", check=check, timeout=30.0)
    except TimeoutError:
        await ctx.send("Время вышло. Задача не решена.")
        return 0

    user_answer = user_answer.content

    if user_answer == correct_answer:
        await ctx.send("Правильно!")
        return 1
    else:
        await ctx.send(f"Неправильно! Правильный ответ: {correct_answer}")
        return 0


async def geometry_task(ctx, task_number):
    question_data = random.choice(geometry_questions)
    correct_answer = question_data["correct_option"]

    await ctx.send(f"(Задача №{task_number}): {question_data['question']}")
    await ctx.send(f"Варианты ответов: {question_data['options']}")

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel

    try:
        user_answer = await bot.wait_for("message", check=check, timeout=1000.0)
    except TimeoutError:
        await ctx.send("Время вышло. Задача не решена.")
        return 0

    user_answer = user_answer.content

    if user_answer == correct_answer:
        await ctx.send("Правильно!")
        return 1
    else:
        await ctx.send(f"Неправильно! Правильный ответ: {correct_answer}")
        return 0


bot.run(config.TOKEN)
