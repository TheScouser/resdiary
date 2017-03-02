from ConfigParser import RawConfigParser

class Config:

        rcfg = RawConfigParser()
        rcfg.read("default.cfg")

        @staticmethod
        def get(sec, name, type=int):
                if type is float:
                        return float(Config.rcfg.get(sec, name))
                return int(Config.rcfg.get(sec, name))

        @staticmethod
        def set(sec, name, value):
                Config.rcfg.set(sec, name, str(value))
                Config.save_changes()

        @staticmethod
        def get_recommenders():
                '''Returns a list of recommenders referenced in the config file.
                Also known as all section names except DEFAULT and System. If
                you want to have 'System' there as well, use Config.rcfg.sections().'''
                recommenders = Config.rcfg.sections()
                recommenders.remove('System')
                return recommenders

        @staticmethod
        def set_weights(weights):
                '''Takes a tuple of weights (in the order of recommenders in
                Config.get_recommenders()) and writes them to the weight
                attributes in each recommender's section.'''
                for recommender, weight in zip(Config.get_recommenders(),
                                               weights):
                        Config.rcfg.set(recommender, 'weight', str(weight))
                Config.save_changes()

        @staticmethod
        def save_changes():
                '''Saves changes to the file. All set methods call this helper
                function. It's more efficient this way.'''
                with open('default.cfg', 'wb') as configfile:
                        Config.rcfg.write(configfile)
