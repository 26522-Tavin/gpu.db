#import sqlite3
import sqlite3

# Set the global database file name variable
DATABASE = "gpu.db"

#functions
def print_gpus_for_animation():
    '''print the first 5 gpus good for animation along with their performance scores'''
    db = sqlite3.connect(DATABASE)  # Open a connection to the 'gpu.db' file
    cursor = db.cursor()  # Create a cursor object to run SQL instructions
    
    # Starts an SQL command that joins the graphics_card table and the performance table together
    sql = """
    SELECT g.gpu_name, g.manufacturer_name, g.vram, g.price, p.benchmark_tool, p.score 
    FROM graphics_card g 
    JOIN performance p ON g.gpu_id = p.gpu_id 
    WHERE g.gpu_id BETWEEN 1 AND 5;
    """

    cursor.execute(sql)  # Run the SQL join query inside the database
    results = cursor.fetchall()  # Grab all 5 matching rows and save them into the results variable
    
    # Print the column headers with clean, left-aligned layout spacing including performance metrics
    print(f"\n{'Name':<36} {'Manufacturer':<14} {'VRAM':<15} {'Price':<10} {'Benchmark Tool':<18} {'Score':<10}")
    print("-" * 108)  # Print a dashed line to separate the headers from the data rows
    
    for gpu in results: #loop the results
        # Index breakdown from our SELECT query: 
        # gpu[0]=Name, gpu[1]=Manufacturer, gpu[2]=VRAM, gpu[3]=Price, gpu[4]=Benchmark Tool, gpu[5]=Score
        print(f"{gpu[0]:<36} {gpu[1]:<14} {gpu[2]:<15} {gpu[3]:<10} {gpu[4]:<18} {gpu[5]:<10}")
        
    db.close()  # Disconnect from the database to clean up system memory
    #stop loop


def print_gpus_for_gaming():
    '''print the second 5 gpus good for gaming along with their performance scores'''
    db = sqlite3.connect(DATABASE)  # Open a connection to the 'gpu.db' file
    cursor = db.cursor()  # Create a cursor object to run SQL instructions
    
    # Define an SQL command that joins the graphics_card table and the performance table together
    sql = """
    SELECT g.gpu_name, g.manufacturer_name, g.vram, g.price, p.benchmark_tool, p.score 
    FROM graphics_card g 
    JOIN performance p ON g.gpu_id = p.gpu_id 
    WHERE g.gpu_id BETWEEN 6 AND 10;
    """
    
    cursor.execute(sql)  # Run the SQL join query inside the database
    results = cursor.fetchall()  # Grab all 5 matching rows and save them into the results variable
    
    # Print the column headers with clean, left-aligned layout spacing including performance metrics
    print(f"\n{'Name':<36} {'Manufacturer':<14} {'VRAM':<15} {'Price':<10} {'Benchmark Tool':<18} {'Score':<10}")
    print("-" * 108)  # Print a dashed line to separate the headers from the data rows
    
    for gpu in results: #loop the results
        # Index breakdown from our SELECT query: 
        # gpu[0]=Name, gpu[1]=Manufacturer, gpu[2]=VRAM, gpu[3]=Price, gpu[4]=Benchmark Tool, gpu[5]=Score
        print(f"{gpu[0]:<36} {gpu[1]:<14} {gpu[2]:<15} {gpu[3]:<10} {gpu[4]:<18} {gpu[5]:<10}")
        
    db.close()  # Disconnect from the database to clean up system memory
    #stop loop


def print_gpus_for_office():
    '''print the last 5 gpus good for office work along with their performance scores'''
    db = sqlite3.connect(DATABASE)  # Open a connection to the 'gpu.db' file
    cursor = db.cursor()  # Create a cursor object to run SQL instructions
    
    # Define an SQL command that joins the graphics_card table and the performance table together
    sql = """
    SELECT g.gpu_name, g.manufacturer_name, g.vram, g.price, p.benchmark_tool, p.score 
    FROM graphics_card g 
    JOIN performance p ON g.gpu_id = p.gpu_id 
    WHERE g.gpu_id BETWEEN 11 AND 15;
    """
    
    cursor.execute(sql)  # Run the SQL join query inside the database
    results = cursor.fetchall()  # Grab all 5 matching rows and save them into the results variable
    
    # Print the column headers with clean, left-aligned layout spacing including performance metrics
    print(f"\n{'Name':<36} {'Manufacturer':<14} {'VRAM':<15} {'Price':<10} {'Benchmark Tool':<18} {'Score':<10}")
    print("-" * 108)  # Print a dashed line to separate the headers from the data rows
    
    for gpu in results: #loop the results
        # Index breakdown from our SELECT query: 
        # gpu[0]=Name, gpu[1]=Manufacturer, gpu[2]=VRAM, gpu[3]=Price, gpu[4]=Benchmark Tool, gpu[5]=Score
        print(f"{gpu[0]:<36} {gpu[1]:<14} {gpu[2]:<15} {gpu[3]:<10} {gpu[4]:<18} {gpu[5]:<10}")
        
    db.close()  # Disconnect from the database to clean up system memory
    #stop loop


#main code
while True:
    # Prompt the user with a text menu and capture their numeric input choice
    user_input = input("""\nWhat would you like to do?
        1. Find GPUs good for Animation.
        2. Find GPUs good for Gaming.
        3. Find GPUs good for Office Work.
        4. Exit
        
    Enter your choice (1-4): """)

    if user_input == "1":  # Check if the user typed choice "1"
        print_gpus_for_animation()  # Trigger the animation filter function
    elif user_input == '2':  # Check if the user typed choice "2"
        print_gpus_for_gaming()  # Trigger the gaming filter function
    elif user_input == '3':  # Check if the user typed choice "3"
        print_gpus_for_office()  # Trigger the office work filter function
    elif user_input == '4':  # Check if the user typed choice "4"
        print("\nExiting program. Goodbye!")  # Display a friendly departure note
        break  # Shut down the while loop to terminate the program execution
    else:  # Capture any invalid text or unexpected number keys entered by the user
        print("That was not an option\n")  # Show an error notification message
        break  # Stop the infinite loop safely