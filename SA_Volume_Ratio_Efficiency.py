import math
print('Cellular Surface Area-to-Volume Ratio Simulator')
shape = input('Specimen Shape (Cuboidal, Cylindrical, Spherical) = ').lower().strip()
Surface_Area = 0.0
Volume = 0.0

if shape == 'cuboidal':
    Length = float(input('Length (µm) = '))
    Breadth = float(input('Breadth (µm) = '))
    Height = float(input('Height (µm) = '))
    Surface_Area = 2 * (Length * Breadth + Breadth * Height + Height * Length)
    Volume = Length * Breadth * Height

elif shape == 'cylindrical':
    Length = float(input('Length (µm) = '))
    Radius = float(input('Radius (µm) = '))
    Surface_Area = 2 * math.pi * Radius * (Radius + Length)
    Volume = math.pi * Radius**2 * Length

elif shape == 'spherical':
    Radius = float(input('Radius (µm) = '))
    Surface_Area = 4 * math.pi * Radius**2
    Volume = 4/3 * math.pi * Radius**3

print(f'Surface Area = {Surface_Area:.2f} square units')
print(f'Volume = {Volume:.2f} cubic units')

Surface_To_Volume_Ratio = Surface_Area / Volume
print(f'Surface To Volume Ratio = {Surface_To_Volume_Ratio:.2f}')
if Surface_To_Volume_Ratio >= 3:
    print('Generated Surface To Volume Ratio Indicates High Efficiency Specimen Structure Indicating Excellent Diffusion Potential.')
elif Surface_To_Volume_Ratio <= 1:
    print('Generated Surface To Volume Ratio Indicates Poor Efficiency Specimen Structure Indicating Requirement Of Adaptations.')
else:
    print('Generated Surface To Volume Ratio Indicates Moderate To Low Specimen Structure Indicating Good To Limited Diffusion Potential.')
 

