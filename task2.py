from dataclasses import dataclass

EPSILON=1e-3
KELVIN_OFFSET=273.15

@dataclass
class Temperatures:
    celsius_temperature:float=0.0
    kelvin_temperature:float=0.0
    farenheit_temperature:float=0.0

    def __str__(self) -> str:
        if abs(self.celsius_temperature)<EPSILON:
            return (f'{self.celsius_temperature:<22.2e}  {self.kelvin_temperature:<22.2f}  {self.farenheit_temperature:<22.2f}')

        if abs(self.kelvin_temperature)<EPSILON:
            return (f'{self.celsius_temperature:<22.2f}  {self.kelvin_temperature:<22.2e}  {self.farenheit_temperature:<22.2f}')

        if abs(self.farenheit_temperature)<EPSILON:
            return (f'{self.celsius_temperature:<22.2f}  {self.kelvin_temperature:<22.2f}  {self.farenheit_temperature:<22.2e}')

        return (f'{self.celsius_temperature:<22.2f}  {self.kelvin_temperature:<22.2f}  {self.farenheit_temperature:<22.2f}')



def get_parametr()->tuple[float,str]:

    while True:
        temperature_measure=input("Enter in what measure you wanna input (c) celsius (k) kelvins (f) farenheit: ")
        if temperature_measure != 'c' and temperature_measure != 'k' and temperature_measure !='f':
            print('Invalid measure TRY AGAIN!!!')
        else:
            break
    while True:
        try:
            
            temperature=float(input('Enter start temperature: '))

    
        except ValueError as error:
            print(error,' try again!')

        else:
            if(temperature<-KELVIN_OFFSET and temperature_measure=='c') or (temperature<0 and temperature_measure=='k') or (temperature<-459.67 and temperature_measure=='f'):
                print("Your temperature is too low!!!")
                continue

            print(f'You entered temperature: {temperature}')
            break

    return (temperature,temperature_measure)




def recalculate_temperature()->Temperatures:
    start_temperature,temperature_measure=get_parametr()


    match temperature_measure:
        case 'c':
            kelvin_temperature=start_temperature+KELVIN_OFFSET
            farenheit_temperature=start_temperature*1.8 +32
            return Temperatures(start_temperature,kelvin_temperature,farenheit_temperature)

        case 'k':
            celsius_temperature=start_temperature-KELVIN_OFFSET
            farenheit_temperature=start_temperature*1.8 -459.67
            return Temperatures(celsius_temperature,start_temperature,farenheit_temperature)

        case 'f':
            celsius_temperature=(start_temperature-32)/1.8
            kelvin_temperature=(start_temperature-32)/1.8 +KELVIN_OFFSET
            return Temperatures(celsius_temperature,kelvin_temperature,start_temperature)

        case _:
            raise ValueError(f'Unknown measure {temperature_measure}')
        


if __name__=='__main__':


    temperatures1=Temperatures()
    temperatures2=Temperatures()
    temperatures3=Temperatures()
    temperatures1=recalculate_temperature()
    temperatures2=recalculate_temperature()
    temperatures3=recalculate_temperature()
    print(f'{'Celsius_temperature':<22} {'Kelvin_temperature':<22} {'Farenheit_temperature':<22}',
                temperatures1,temperatures2,temperatures3,sep='\n')


    temp1=Temperatures()





print("The end!!!")