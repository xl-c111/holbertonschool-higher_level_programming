import os

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Template must be a string.")
        return
    
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Attendees must be a list of  dictionaries.")
        return
    
    if not template:
        print("Template must not be empty.")
        return
    
    if not attendees:
        print("Attendees must not be empty.")
        return
    
    for i, attendee in enumerate(attendees, start=1):
        personalized = template
        for placeholder in ['name', 'event_title', 'event_date', 'event_location']:
            value = attendee.get(placeholder, "N/A")
            personalized = personalized.replace(f"{{{placeholder}}}", value)
    
        output_filename = f"output_{i}.txt"
    
        try:
            with open(output_filename, "w", encoding="utf-8") as f:
                f.write(personalized)
            print(f"Written: {output_filename}")
        except Exception as e:
            print(f"Error writing to {output_filename}: {e}")




