from environs import Env



env = Env()
env.read_env()


BOT_TOKEN = env('BOT_TOKEN')

ADMIN_ID = env('ADMIN_ID')


GROUP_ID = env('GROUP_ID')