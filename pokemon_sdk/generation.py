from utils import api_get

class GenerationClient:
    def __init__(self):
        pass

    def get_generations_list(self,limit=20,offset=0):
        endpoint = 'generation'
        params = {'limit': limit,'offset':offset}
        data=api_get(endpoint, params)
        return data
    
    def get_generation(self, identifier):
        endpoint = f'generation/{identifier}'
        data = api_get(endpoint)
        return data
    
    #Paginton
    def get_all_generations(self):
        all_generations = []
        limit = 20
        offset = 0
        while True:
            data = selg.get_generations_list(limit=limit,offset=offset)
            all_generations.extend(data['results'])
            if data['next'] is None:
                break
            offset += limit
        return all_generations