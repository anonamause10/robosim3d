from distutils.core import setup
setup(
  name = 'robosim3d',         # How you named your package folder (MyLib)
  packages = ['robosim3d'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Library for interacting with my RoboSim app',   # Give a short description about your library
  author = 'Arjun Pal',                   # Type in your name
  author_email = 'pal.arjun170@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/anonamause10/robosim3d',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/anonamause10/robosim3d/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['Simulator', 'Robotics', 'KEYWORDS'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
        
      ],
  classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: End Users/Desktop',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)