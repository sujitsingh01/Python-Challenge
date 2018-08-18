import os, csv
voterid= []
county =[]
candidates = []
result = []
vote_count = 0
total_votes = 0
unique_candidate = []
max_count = 0
winner = ' '


input_file = os.path.join('election_data.csv')
output_file = os.path.join('election_data_analysed.csv')

with open (input_file, 'r',newline='') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    header = next(reader)

    for row in reader:
        voterid.append(row[0])
        county.append(row[1])
        candidates.append(row[2])

    total_votes = len(voterid)
    unique_candidate = set(candidates)

    with open(output_file,'w') as out_file:
        print('Election Results')
        print('Election Results', file=out_file)
        print('-------------------------------')
        print('-------------------------------',file = out_file)
        print(f'Total Votes :  {(total_votes)}')   
        print(f'Total Votes :  {(total_votes)}',file = out_file)    
        print('-------------------------------')
        print('-------------------------------',file=out_file)

        for cand in unique_candidate:
            for cand2 in candidates:
                if (cand2 == cand):
                    vote_count +=1

            if (vote_count > max_count):
                max_count = vote_count  
                winner = cand

            percent = round((vote_count/total_votes)*100 ,2)

            print(f'{cand} : {percent}% ({vote_count})') 
            print(f'{cand} : {percent}% ({vote_count})',file=out_file) 
            
            vote_count = 0

        print('-------------------------------',file = out_file)
        print('-------------------------------')
        print(f'Winner : {winner}')
        print(f'Winner : {winner}',file = out_file)
        print('-------------------------------',file = out_file)
        print('-------------------------------')    
    
   
    
    