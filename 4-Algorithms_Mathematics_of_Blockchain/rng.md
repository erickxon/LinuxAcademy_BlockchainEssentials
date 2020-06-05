# Random Number Generation
```
- an important aspect of cryptography
- not so simple as human RNG when it comes to computer RNG
    - finite state machines and there is instruction for everything: impossible to generate true random numbers
    - impossible to generate a truly random number 
        - pseudo-random numbers (PRNG) instead
            - choosing a seed (TIME, human immune system, subatomic particles)
                - obtained by some measurement
            - multiply seed by itself
            - from the product, all digitas between the first and last digits are taken and this represents a new number
            - this number is then multiplied by itself and the process is repeated as many times as needed
            - sequence will eventually repeat certainly once the first seed occurs again
                - the bigger the initial seed, the smaller the chance the sequence will repeat
- random processes are non-deterministic: impossible to determine in advance
- random number generators that produce true random numbers are called hardware RNG
    - obtains these by measuring natural processes (noise, photoelectric effect, etc)
- machine processes are determinisitc: the way they operate is predictable and repeatable
- randomness increases security
```