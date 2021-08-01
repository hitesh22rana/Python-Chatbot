import random
import re

insulin = 'Insulin is a peptide hormone produced by beta cells of the pancreatic islets; it is considered to be the main anabolic hormone of the body. It regulates the metabolism of carbohydrates, fats and protein by promoting the absorption of glucose from the blood into liver, fat and skeletal muscle cells.'

type_of_diabetes = '''Diabetes is a chronic disease that occurs when the pancreas is no longer able to make insulin, or when the body cannot make good use of the insulin it produces.

Type 1 diabetes can develop at any age, but occurs most frequently in children and adolescents. When you have type 1 diabetes, your body produces very little or no insulin, which means that you need daily insulin injections to maintain blood glucose levels under control.

Type 2 diabetes is more common in adults and accounts for around 90% of all diabetes cases. When you have type 2 diabetes, your body does not make good use of the insulin that it produces. The cornerstone of type 2 diabetes treatment is healthy lifestyle, including increased physical activity and healthy diet. However, over time most people with type 2 diabetes will require oral drugs and/or insulin to keep their blood glucose levels under control.

Gestational diabetes (GDM) is a type of diabetes that consists of high blood glucose during pregnancy and is associated with complications to both mother and child. GDM usually disappears after pregnancy but women affected and their children are at increased risk of developing type 2 diabetes later in life.
'''

blood_sugar_level = '''A blood sugar level less than 140 mg/dL (7.8 mmol/L) is normal. A reading of more than 200 mg/dL (11.1 mmol/L) after two hours indicates diabetes.'''

vision = '''A reference value above which visual acuity is considered normal is called 6/6 vision, the USC equivalent of which is 20/20 vision: At 6 metres or 20 feet, a human eye with that performance is able to separate contours that are approximately 1.75 mm apart. Vision of 6/12 corresponds to lower performance, while vision of 6/3 to better performance. Normal individuals have an acuity of 6/4 or better (depending on age and other factors). '''

nutrition = '''Nutrition is the biochemical and physiological process by which an organism uses food to support its life. It includes ingestion, absorption, assimilation, biosynthesis, catabolism and excretion. The science that studies the physiological process of nutrition is called nutritional science.'''

def thanks():
    response = ['Thank you!!','Glad I could help you!!','Thanks a lot'][random.randrange(3)]
    return response

def unknown():
    response = ['could you please re-phrase that?',
               "Didn't get what you are saying ", 
               'Sorry!! can you write it again!!',
               'Oh!! i did not get that , come again!!'][random.randrange(4)]
    return response

def symptoms(query):
    if ('weight' and 'loss') in query or 'thirst' in query or 'urination' in query or 'fatigue' in query or ('blurred' and 'vision') in query:
        print("You may have some symptoms of Diabetes, but it is too early to conclude that you have Diabetes. so you may contact to the doctor.")
    elif ('fever' in query or 'cold' in query or 'vomit' in query):
        print("You may seem to have some viral infection. Kindly, concern the doctor for checkup")
    else:
        print("You may seem to have other symptoms than of diabetes. But, You may get check by Doctor")

def symptoms_input():
    print("Please tell us all the symptoms you are having")
    print(">> ",end="")
    query = str(input(""))
    ans = re.split(r'\s+|[,;?!.-]\s*', query.lower())
    symptoms(ans)