from dataclasses import dataclass


@dataclass
class Temperatures:
    celsius_temperature:float=0.0
    kelvin_temperature:float=0.0
    farenheit_temperature:float=0.0

    def __str__(self) -> str:
        if abs(self.celsius_temperature)<1e-3:
            return (f'{self.celsius_temperature:<22.2e}  {self.kelvin_temperature:<22.2f}  {self.farenheit_temperature:<22.2f}')

        if abs(self.kelvin_temperature)<1e-3:
            return (f'{self.celsius_temperature:<22.2f}  {self.kelvin_temperature:<22.2e}  {self.farenheit_temperature:<22.2f}')

        if abs(self.farenheit_temperature)<1e-3:
            return (f'{self.celsius_temperature:<22.2f}  {self.kelvin_temperature:<22.2f}  {self.farenheit_temperature:<22.2e}')
        
        

        return (f'{self.celsius_temperature:<22.2f}  {self.kelvin_temperature:<22.2f}  {self.farenheit_temperature:<22.2f}')



def get_parametr(celsius:bool=False,kelvin:bool=False,farenheit:bool=False)->float:
    while True:
        try:
            temperature=float(input('Enter temperature: '))
    
        except ValueError as error:
            print(error,' try again!')

        else:
            if(temperature<-273.15 and celsius==True) or (temperature<0 and kelvin==True) or (temperature<-459.67 and farenheit==True):
                print("Your temperature is too low!!!")
                continue

            print(f'You entered temperature: {temperature}')
            break

    return temperature


def celsius_recalculation(celsius_temperature:float)->Temperatures:

    kelvin_temperature=celsius_temperature+273.15
    farenheit_temperature=celsius_temperature*1.8 +32
    return Temperatures(celsius_temperature,kelvin_temperature,farenheit_temperature)


def kelvin_recalculation(kelvin_temperature:float )->Temperatures:

    celsius_temperature=kelvin_temperature-273.15
    farenheit_temperature=kelvin_temperature*1.8 -459.67
    return Temperatures(celsius_temperature,kelvin_temperature,farenheit_temperature)


def farenheit_recalculation(farenheit_temperature:float)->Temperatures:

    celsius_temperature=(farenheit_temperature-32)/1.8
    kelvin_temperature=(farenheit_temperature-32)/1.8 +273.15
    return Temperatures(celsius_temperature,kelvin_temperature,farenheit_temperature)


if __name__=='__main__':


    temperatures1=Temperatures()
    temperatures2=Temperatures()
    temperatures3=Temperatures()
    temperatures1=celsius_recalculation(get_parametr(celsius=True))
    temperatures2=kelvin_recalculation(get_parametr(kelvin=True))
    temperatures3=farenheit_recalculation(get_parametr(farenheit=True))
    print(f'{'Celsius_temperature':<22} {'Kelvin_temperature':<22} {'Farenheit_temperature':<22}',
                temperatures1,temperatures2,temperatures3,sep='\n')

print("The end!!!")