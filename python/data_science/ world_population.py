import json
from pygal_maps_world.i18n import COUNTRIES
import pygal
from pygal.style import RotateStyle
from pygal.style import LightColorizedStyle

filename = '/home/carlos_/Desktop/Projects/Python/Analise-Dados/Downloading-Data/population_data.json'

def get_country_code(country_name):
    for code, name in COUNTRIES.items():
        if name == country_name: 
            return code
        
    return None

def wp():

    with open(filename) as f: 
        pop_data = json.load(f)
        cc_populations = {}
        for pop_dict in pop_data: 
            if pop_dict['Year'] == '2010':
                country_name = pop_dict['Country Name']
                population = int(float(pop_dict['Value']))

                code = get_country_code(country_name)
                
                if code:
                    cc_pops_1, cc_pops_2,cc_pops_3 = {}, {}, {}
                    #verificar a população de cada país
                    for cc, pop in cc_populations.items(): 
                        if pop < 10000000: 
                            cc_pops_1[cc]= pop 
                        elif pop < 1000000000: 
                            cc_pops_2[cc] = pop 
                        else: 
                            cc_pops_3[cc] = pop

                    # Vê quantos países estão em cada nível w print(len(cc_pops_1),
                    print(len(cc_pops_1),len(cc_pops_2), len(cc_pops_3))
                    #print(code + ": "+str(population)) 

                    cc_populations[code] = population

                    wm_style = RotateStyle('#205698', base_style=LightColorizedStyle)
                    wm = pygal.maps.world.World(style=wm_style)
                    
                    wm.title = 'World Population in 2010, by Country'
                    wm.add('0-10m', cc_pops_1) 
                    wm.add('10m-1bn', cc_pops_2) 
                    wm.add('>1bn',cc_pops_3)
                    wm.render_to_file('americas.svg')
                
                #else: 
                    #print('ERROR - ' + country_name)    
            
# Transforma o codigo 
def countries():
    with open(filename) as f: 
        pop_data = json.load(f)
        for country_code in sorted(COUNTRIES.keys()): 
            print(country_code,COUNTRIES[country_code])




def mpM():
    wm = pygal.maps.world.World()
    wm.title = 'North, Central, and South America'
    wm.add('North America', {'ca': 34126000, 'us': 309349000, 'mx':113423000})
    wm.add('Central America',['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv']) 
    wm.add('South America', ['ar','bo', 'br', 'cl', 'co', 'ec', 'gf', 'gy', 'pe', 'py', 'sr', 'uy', 've'])
    wm.render_to_file('americas.svg')




wp()