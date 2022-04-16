# anarchy-for-her

A PiTank project, inspired by [HanYangZhao's Cannon Robot build](http://www.instructables.com/id/PiTank-A-web-controlled-tank-with-real-time-video-/); repository can be found [here](https://github.com/HanYangZhao/CannonRobot). 

Made during the 2021-2022 school year for Bayview Robotics while we got an FTC team started up :D

![image](https://cdn.discordapp.com/attachments/914745005346811924/920447237308420156/IMG_1701.png)  
![image](https://cdn.discordapp.com/attachments/914745005346811924/920447237643972619/IMG_1698.png)

## Materials
Fueled by:
- [Waterbottle](https://www.amazon.ca/gp/product/B001NCDE8O/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1) (to act as the fuel chamber)
- PVC Pipe + T-connector (Home Depot)
    - The other workaround is to get the person with a 3d printer to make a rifled barrel :D
- Sparklighter (for the combustion with fuel)
- Duct tape (no explanation needed)
- Epoxy
- AXE's [Anarchy for Her Body Spray](https://www.amazon.ca/Axe-Anarchy-Daily-Fragrance-113g/dp/B009EC4ET8/ref=sr_1_9?crid=12NDWDR5TJ086&keywords=axe%2Banarchy%2Bfor%2Bher%2Bbody%2Bspray&qid=1650038721&sprefix=axe%2Banarchy%2Bfor%2Bherbody%2Bspray%2Caps%2C71&sr=8-9&th=1) | [Dark Temptation Body Spray](https://www.amazon.ca/Dark-Temptation-Daily-Fragrance-113g/dp/B01B1DN650/ref=sr_1_4_sspa?keywords=axe+dark+temptation+body+spray&qid=1637615062&sr=8-4-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFHTlBGMk5OUVJEQjUmZW5jcnlwdGVkSWQ9QTA3NzcxNjMyTzlTMkwwRVVDUUxHJmVuY3J5cHRlZEFkSWQ9QTAwMTY4MzVXTUw2WlpURklOWlImd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl)  
- The old VEX V4 kits our school has (for chassis)
- VEX 393 motors + motor controllers (4)
- at least one fire extinguisher 
- Amazon Prime
- [Raspberry Pi 3B](https://www.canakit.com/raspberry-pi-3-model-b-plus.html)
- [PiSugar Battery Pack](https://www.amazon.ca/Pisugar2-Portable-Platform-Raspberry-Accessories/dp/B08D8PPCKN/ref=cm_cr_arp_d_product_top?ie=UTF8)
- the materials that come in an [Arduino starter kit](https://www.amazon.ca/Elegoo-Project-Starter-Tutorial-Arduino/dp/B01D8KOZF4/ref=asc_df_B01D8KOZF4/?tag=googleshopc0c-20&linkCode=df0&hvadid=292968375828&hvpos=&hvnetw=g&hvrand=6903158297644869653&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9000792&hvtargid=pla-406302474425&psc=1)
- Fred's 3D printer
- [Servos](https://www.amazon.ca/gp/product/B07VT5T9JC/ref=ox_sc_act_title_2?smid=A2FI4MJY3VQVX5&psc=1)
- [Wires](https://www.amazon.ca/Premium-Breadboard-Jumper-100-Pack-Hellotronics/dp/B07ZHXPQWS?th=1)
- [Solenoids](https://www.amazon.ca/gp/product/B07Y5TVG6Z/ref=ox_sc_act_title_1?smid=A2KRDQ1AI5Y5G6&psc=1)
- Stepper Motor stuff


## Process
We had to majorly revamp the entire process. Pretty much none of us knew how to do anything, and the project was already 7 years old so the code was all outdated and most of the hardware listed wasn't available for purchase. 

### Differences
1. RIP arduino
2. Since we needed to run this in the school, we needed to find a workaround to getting the Pi connected to the wifi (static ip would not work)
    - Configure Bluetooth on the Pi

### Issue Documentation
Here are a few issues that we ran into:
<details>
<summary>Getting funds for this project</summary>
Robotics is incredibly expensive. The school being out of funds for 2 years also didn't help, so we applied to a grant to buy parts for both this project and for future club use :D
</details>

<details>
<summary>Sparklighter issues</summary>

+ <details>
    <summary>Not sparking</summary>
    Make sure the wires are not crossed so the current doesn't jump
  </details> 

+ <details>
    <summary>Residue on the conductors</summary>
    Scrape it off with a knife/clean it with rubbing alcohol
  </details>
</details>

<details>
<summary>Figuring out how motors and servos work</summary>
There's an ungodly amount of trial and error involved here, but the main takeaway was to simply test code to see if it worked. 
<br></br>
Motors and servos receive signals, or a PWM value, as instruction. PWM is pulse width modulation, meaning it will pulse a signal with a certain frequency to relay instruction. After sitting down with the VEX motors for 4 excruciating hours, I found that the PWM values it took were from between 6-22 by running a loop with PWM output from 1-100 and observing the behavior (direction, speeds). 
</details>

<details>
<summary>The cannon barrel/chamber popping off during the combustion</summary>
This just means that the AXE:oxygen ratio was perfect. Concluded that AXE can be used as butane.
<br></br>
Also figured out that using epoxy over duct tape might've been a better idea 
</details>

<details>
<summary>Condensation/concentration of the AXE preventing sparking</summary>
Chopstick + paper towel :D
<br></br>
On a more serious note, the environment/temperature of the room where you're firing plays a huge role. As Canadians we're at a clear disadvantage
<br></br>
As suggested, adding some sort of ventilation would work, probably a fan 
</details>

## Tank Media
![image](https://cdn.discordapp.com/attachments/754151523600039959/947550928356122664/IMG_2963.png)  
[a video](https://cdn.discordapp.com/attachments/488107788329943042/964552199428517918/cannon5.mp4)  
