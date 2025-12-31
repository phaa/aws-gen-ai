import os
import json
import sqlite3
from datetime import datetime

def get_available_vacations_days(employee_id):
    
    conn = sqlite3.connect('employee_database.db')
    c = conn.cursor()

    if not employee_id:
        conn.close()
        raise ValueError("Employee ID is required")

    c.execute("""
        SELECT employee_vacation_days_available
        FROM vacations
        WHERE employee_id = ?
        ORDER BY year DESC
        LIMIT 1
    """, (str(employee_id),))

    result = c.fetchone()
    conn.close()

    if result:
        return result[0]
    else:
        return f"No vacation data found for employee_id {employee_id}"

def lambda_handler(event, context):
    try:
        print(f"Received event: {json.dumps(event)}")
        
        # Bedrock Agent passa parâmetros em diferentes formatos
        employee_id = None
        
        # Tentar diferentes formatos de entrada
        if 'employee_id' in event:
            employee_id = event['employee_id']
        elif 'parameters' in event:
            for param in event['parameters']:
                if param['name'] == 'employee_id':
                    employee_id = param['value']
                    break
        
        if not employee_id:
            raise ValueError("employee_id parameter is required")
        
        available_days = get_available_vacations_days(employee_id)
        
        # Formato de resposta para Bedrock Agent
        response = {
            'response': {
                'actionGroup': event.get('actionGroup', 'VacationsActionGroup'),
                'function': event.get('function', 'get_available_vacations_days'),
                'functionResponse': {
                    'responseBody': {
                        'TEXT': {
                            'body': json.dumps({
                                'employee_id': employee_id,
                                'available_vacation_days': available_days
                            })
                        }
                    }
                }
            }
        }
        
        print(f"Returning response: {json.dumps(response)}")
        return response
        
    except Exception as e:
        print(f"Error: {str(e)}")
        
        # Formato de erro para Bedrock Agent
        error_response = {
            'response': {
                'actionGroup': event.get('actionGroup', 'VacationsActionGroup'),
                'function': event.get('function', 'get_available_vacations_days'),
                'functionResponse': {
                    'responseBody': {
                        'TEXT': {
                            'body': json.dumps({
                                'error': str(e)
                            })
                        }
                    }
                }
            }
        }
        
        return error_response