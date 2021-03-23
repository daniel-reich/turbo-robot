"""


When escaping a compound system, such as a moon orbiting a planet or a planet
orbiting a sun, a rocket that leaves at escape velocity (ve1) for the first
(orbiting) body, (e.g. Earth) will not travel to an infinite distance because
it needs an even higher speed to escape gravity of the second body (e.g. the
Sun). Near the Earth, the rocket's trajectory will appear parabolic, but it
will still be gravitationally bound to the second body and will enter an
elliptical orbit around that body, with an orbital speed similar to the first
body.

To escape the gravity of the second body once it has escaped the first body
the rocket will need to be travelling at the escape velocity for the second
body (ve2) (at the orbital distance of the first body). However, when the
rocket escapes the first body it will still have the same orbital speed around
the second body that the first body has. So its excess velocity as it escapes
the first body will need to be the difference between the orbital velocity and
the escape velocity. With a circular orbit, escape velocity is √2 times the
orbital speed.

### Objective

Create a function that takes a planet as an argument and returns the escape
velocity from the system Planet/Sun expressed in km/s, as well as the ratio
between the calculated escape velocity from the system Planet/Sun and the
escape velocity from the system Earth/Sun.

### Data

In the following table you will find for each planet its escape velocity
relative to its own gravity and the escape velocity relative to the the Sun's
gravity (at the corresponding orbital distance of the planet).

Planet| ve1| ve2  
---|---|---  
Mercury| 4.25| 67.7  
Venus| 10.36| 49.5  
Earth| 11.186| 42.1  
Mars| 5.03| 34.1  
Jupiter| 60.20| 18.5  
Saturn| 36.09| 13.6  
Uranus| 21.38| 9.6  
Neptune| 23.56| 7.7  
  
Consider:

    k = 0.2929

### Examples

    system_escape_velocity("Mercury") ➞ "The escape velocity from the system Mercury/Sun is 20.3 km/s. The escape velocity from the system Mercury/Sun is 1.2 times the escape velocity from the system Earth/Sun."
    
    system_escape_velocity("Earth") ➞ "The escape velocity from the system Earth/Sun is 16.6 km/s. The escape velocity from the system Earth/Sun is 1.0 times the escape velocity from the system Earth/Sun."

### Notes

  * Round to the nearest tenth the escape velocity from the system Planet/Sun. Do not round the the escape velocity from the system Earth/Sun to calculate the ratio between escape velocities, but round the ratio to the nearest tenth.
  * See part #1 of this series: [Escape Velocity I](https://edabit.com/challenge/WpjKZ54MgfMbjoWKi).

"""

ev = {
    'Mercury': (4.25, 67.7), 'Venus': (10.36, 49.5), 'Earth': (11.186, 42.1),
    'Mars': (5.03, 34.1), 'Jupiter': (60.20, 18.5), 'Saturn': (36.09, 13.6),
    'Uranus': (21.38, 9.6), 'Neptune': (23.56, 7.7)
}
def system_escape_velocity(planet):
    k = 0.2929
    v1, v2 = ev['Earth']
    earth_sun = pow(v1 * v1 + v2 * v2 * k * k, 0.5)
    vp1, vp2 = ev[planet]
    planet_sun = round(pow(vp1 * vp1 + vp2 * vp2 * k * k, 0.5), 1)
    ratio = round(planet_sun / earth_sun, 1)
    return ('The escape velocity from the system {}/Sun is {} km/s.\n'.format(planet, planet_sun) +
            'The escape velocity from the system {}/Sun is {} times the escape velocity from the system Earth/Sun.'.format(planet, ratio))

