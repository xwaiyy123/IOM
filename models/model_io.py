class ModelOptions:
    def __init__(self, params=None):
        self.params = params


class ModelInput:
    """ Input to the model. """

    def __init__(
            self, state=None, hidden=None, target_class_embedding=None, action_probs=None, states_memory=None,
            action_memory=None, states_rep=None, obs_reps=None, depth=None, glove=None, scene=None, target_object=None,
            nav_graph=None, coord = None, start_coord=None, coord_memory = None, actions = None,last_action_success = None,
            imp_obstacle_map = None, obstacle_index = None):
        self.state = state
        self.hidden = hidden
        self.target_class_embedding = target_class_embedding
        self.action_probs = action_probs
        self.states_memory = states_memory
        self.action_memory = action_memory
        self.states_rep = states_rep
        self.obs_reps = obs_reps
        self.depth = depth
        self.glove = glove
        self.scene = scene
        self.target_object = target_object
        self.nav_graph = nav_graph
        self.coord = coord
        self.start_coord = start_coord
        self.coord_memory = coord_memory
        self.actions = actions
        
        self.last_action_success = last_action_success
        self.imp_obstacle_map = imp_obstacle_map
        self.obstacle_index = obstacle_index



class ModelOutput:
    """ Output from the model. """

    def __init__(self, value=None, logit=None, hidden=None, state_representation=None, embedding=None,
                 state_memory=None, action_memory=None, meta_action=None, visual_info=None, obs_rep=None, match_score=None,
                 nav_graph=None, start_coord=None, coord_memory = None, imp_obstacle_map = None, obstacle_index=None):
        self.value = value
        self.logit = logit
        self.hidden = hidden
        self.state_representation = state_representation
        self.embedding = embedding
        self.state_memory = state_memory
        self.action_memory = action_memory
        self.meta_action = meta_action
        self.visual_info = visual_info,
        self.obs_rep = obs_rep
        self.match_score = match_score
        self.nav_graph = nav_graph
        self.start_coord = start_coord
        self.coord_memory = coord_memory
        
        self.imp_obstacle_map = imp_obstacle_map
        self.obstacle_index = obstacle_index
