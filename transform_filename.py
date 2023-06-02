def transform_filenames(source_filenames):
    object_filenames= []
    #iterating over source filenames
    for filename in source_filenames:
        #extracting the base name from file name without extension
        base_filename = filename.rsplit('.',1)[0]
        
        #replacing the extension with '.o' and append to objectfilenames
        object_filename = base_filename + '.o'
        object_filenames.append(object_filename)
        
    if all(filename.endswith('.o') for filename in object_filenames):
            return object_filenames
    else:
            print('Error: Invalid Object File Extension found')
            return []
    
    
#example usage of this fun 
source_filenames = ['example.c', 'test.cpp', 'program.f', 'code.C', 'file.cxx']
object_filenames = transform_filenames(source_filenames)
print(object_filenames)
        
        
    