from rest_framework.test import APITestCase
from feature_toggle.models import FeatureToggle

def create_feature_toggle_record(name, desc, state):
    return FeatureToggle.objects.create(name=name, desc=desc, state=state)

# Create your tests here.
class TestFeatureToggleCreateView(APITestCase):
    def setUp(self):
        pass
    
    def test_case_1_positive(self):
        '''
        simple test
        it creates feature toggles from data (name, desc, state)
        '''
        resp = self.client.post('/api/v1/feature_toggles/', data={'name': 'abc1', 'desc': 'description', 'state': 'enabled'}, format='json')
        self.assertEqual(resp.status_code, 201)
        expected_data = {"name":"abc1","desc":"description","state":"enabled", "id": 1}
        self.assertEqual(resp.data, expected_data)
        
    def test_case_1_negative(self):
        '''
        try to recreate feature toggles for same name. 
        it should return 400 because name field has unique constraint on it
        '''
        resp = self.client.post('/api/v1/feature_toggles/', data={'name': 'abc1', 'desc': 'description', 'state': 'enabled'}, format='json')
        self.assertEqual(resp.status_code, 201)
        resp = self.client.post('/api/v1/feature_toggles/', data={'name': 'abc1', 'desc': 'description', 'state': 'enabled'}, format='json')
        self.assertEqual(resp.status_code, 400)


class TestFeatureToggleListView(APITestCase):
    def test_case_1_positive(self):
        '''
        simple test
        it creates feature toggles from data (name, desc, state)
        '''
        create_feature_toggle_record('abc1', 'description 1', 'enabled')
        create_feature_toggle_record('abc12', 'description 1', 'enabled')
        resp = self.client.get('/api/v1/feature_toggles/')
        expected_data = [{"id":1,"name":"abc1","desc":"description 1","state":"enabled"},{"id":2,"name":"abc12","desc":"description 1","state":"enabled"}]
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data, expected_data)
        
        
class TestFeatureTogglePartialUpdateView(APITestCase):
    def test_case_1_positive(self):
        '''
        simple test
        try to update fields 
        '''
        rec = create_feature_toggle_record('abc1', 'description 1', 'enabled')
        resp = self.client.patch(f'/api/v1/feature_toggles/{rec.id}/', data={"desc": "changing desc"}, format='json')
        self.assertEqual(resp.status_code, 200)
        expected_data = {"id":1,"name":"abc1","desc":"changing desc","state":"enabled"}
        self.assertEqual(resp.data, expected_data)
        
        
class TestFeatureToggleStateView(APITestCase):
    def test_case_1_positive(self):
        '''
        simple test
        try to toggle state
        '''
        rec = create_feature_toggle_record('abc1', 'description 1', 'enabled')
        self.assertEqual(rec.state, 'enabled')
        resp = self.client.patch(f'/api/v1/feature_toggles/{rec.id}/toggle_state/', format='json')
        self.assertEqual(resp.status_code, 200)
        rec.refresh_from_db()
        self.assertEqual(rec.state, 'disabled')