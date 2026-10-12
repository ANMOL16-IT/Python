import asyncio
from concurrent.futures import ProcessPoolExecutor

def calculate_salary(data):
    name,basic,allowance,deduction = data
    net_salary = basic + allowance - deduction
    return name,net_salary

#Asynchronous function
async def send_notification(name,salary):
    await asyncio.sleep(1)
    print(f"Notification sent to {name}: Salary = {salary}")

#Main asynchronous function
async def main():
    employees = [
        ("Asha",50000,10000,5000),
        ("Rahul",60000,12000,6000),
        ("Priya",45000,8000,4000)
    ]
    with ProcessPoolExecutor(max_workers=2) as executor:
        results = list(executor.map(calculate_salary, employees))
        print("---Payroll Results---")
        for name,salary in results:
            print(f"{name}: Net salary = {salary}")
            tasks = [
                send_notification(name,salary)
                for name,salary in results
            ]
            await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())