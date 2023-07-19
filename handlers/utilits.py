
class ChatId:
    chat_id = 0

    @classmethod
    def set_chat_id(cls, chat_id):
        cls.chat_id = chat_id

    @classmethod
    def get_chat_id(cls):
        return cls.chat_id


class UserNikId:
    user_nik_id = 0

    @classmethod
    def set_user_nik_id(cls, user_nik_id):
        cls.user_nik_id = user_nik_id

    @classmethod
    def get_user_nik_id(cls):
        return cls.user_nik_id


class UserId:
    user_id = 0

    @classmethod
    def set_user_id(cls, user_id):
        cls.user_id = user_id

    @classmethod
    def get_user_id(cls):
        return cls.user_id

class Emoji:
    # https://copychar.cc/emoji/

    CHECK_MARK = "✅"
    STAR = "⭐"
    CROSS_MARK = "❌"

    KEY_KAP_ZERO = "0️⃣"
    KEY_KAP_ONE = "1️⃣"
    KEY_KAP_TWO = "2️⃣"
    KEY_KAP_THREE = "3️⃣"
    KEY_KAP_FOUR = "4️⃣"
    KEY_KAP_FIFE = "5️⃣"

    @classmethod
    def get_check_mark(cls):
        return cls.CHECK_MARK

    @classmethod
    def get_star(cls):
        return cls.STAR

    @classmethod
    def get_cross_mark(cls):
        return cls.CROSS_MARK

    @classmethod
    def get_kap_zero(cls):
        return cls.KEY_KAP_ZERO

    @classmethod
    def get_kap_one(cls):
        return cls.KEY_KAP_ONE

    @classmethod
    def get_kap_two(cls):
        return cls.KEY_KAP_TWO

    @classmethod
    def get_kap_three(cls):
        return cls.KEY_KAP_THREE

    @classmethod
    def get_kap_four(cls):
        return cls.KEY_KAP_FOUR

    @classmethod
    def get_kap_fife(cls):
        return cls.KEY_KAP_FIFE


def getAmojiAndRatinModule(available=False, rating=0):
    module = ""
    avail = "✅" if available else "❌"
    match rating:
        case 0:
            module = avail + " " + Emoji.STAR + " " + Emoji.KEY_KAP_ZERO
        case 1:
            module = avail + " " + Emoji.STAR + " " + Emoji.KEY_KAP_ONE
        case 2:
            module = avail + " " + Emoji.STAR + " " + Emoji.KEY_KAP_TWO
        case 3:
            module = avail + " " + Emoji.STAR + " " + Emoji.KEY_KAP_THREE
        case 4:
            module = avail + " " + Emoji.STAR + " " + Emoji.KEY_KAP_FOUR
        case 5:
            module = avail + " " + Emoji.STAR + " " + Emoji.KEY_KAP_FIFE
    return module
