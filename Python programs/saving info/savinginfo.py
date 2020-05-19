writing_file=open('data_saved.txt', 'w' )
dogs=['bobby', 'scooby', 'misiu', 'rollo', 'tondo', 'tonto']
writing_file.write(', '.join(dogs))
writing_file.close()
