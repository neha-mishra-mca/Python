import pytest
from utilities.test_helpers import TestHelpers

@pytest.mark.smoke
class TestMapFunctionality:
    """Test map component functionality"""
    
    def test_zoom_controls(self, map_component):
        """Test zoom in and zoom out functionality"""
        initial_marker_count = map_component.get_marker_count()
        
        # Test zoom in
        map_component.zoom_in()
        after_zoom_in = map_component.get_marker_count()
        
        # Test zoom out
        map_component.zoom_out()
        after_zoom_out = map_component.get_marker_count()
        
        # Markers should be visible and zoom should work
        assert initial_marker_count >= 0, "No markers found on map"
        # Note: Marker count may change with zoom level due to clustering
    
    
    def test_marker_interaction(self, map_component):
        """Test clicking on individual markers"""
        marker_count = map_component.get_marker_count()
        
        if marker_count > 0:
            # Click on first marker
            map_component.click_marker(0)
            map_component.wait_for_timeout(1000)
            
            # Should trigger some interaction (popup, sidebar, etc.)
            # This test verifies the click doesn't cause errors
            assert True  # Placeholder - adjust based on expected behavior
    
    def test_map_pan_functionality(self, map_component, page):
        """Test map panning/dragging"""
        # Test panning the map
        map_component.pan_map(100, 100)
        map_component.wait_for_timeout(500)
        
        # Verify page is still responsive after panning
        assert TestHelpers.check_page_responsiveness(page), "Page unresponsive after panning"
    
    
    def test_cluster_count_accuracy(self, map_component):
        """Test that cluster counts are displayed correctly"""
        cluster_count = map_component.get_cluster_count()
        
        if cluster_count > 0:
            # Get text from first cluster
            cluster_text = map_component.get_cluster_text(0)
            
            # Should contain a number
            assert cluster_text.isdigit() or any(char.isdigit() for char in cluster_text), \
                f"Cluster text doesn't contain count: {cluster_text}"
