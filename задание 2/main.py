from inherit import Component
from inherit import Processor

def fun():
    inherit = Component(13,23,65,54,65)
    inh = Processor(13,23,65,54,65, 5, 6, 85, 54)
    inherit.get_info()
    inherit.check_compatibility()
    inh.get_info2()
    inh.check_system_compatibility()


def main():
    fun()

if __name__ == '__main__':
    main()