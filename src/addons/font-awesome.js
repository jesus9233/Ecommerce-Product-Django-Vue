import Vue from 'vue'
import { library } from '@fortawesome/fontawesome-svg-core'
import { faShoePrints, faBars, faSearch, faShoppingCart, faStore, faSignInAlt,
         faUserPlus, faCommentAlt, faChevronDown, faBoxOpen, faAward, faThumbsUp,
         faTrashAlt, faMapMarkedAlt, faMobile, faEnvelopeOpenText, faAt, faLock,
         faLockOpen, faEye, faUser
       } from '@fortawesome/free-solid-svg-icons'
import { faFacebookSquare, faTwitterSquare, faInstagram } from '@fortawesome/free-brands-svg-icons'
// import { faThumbsUp as farThumbsUp } from '@fortawesome/pro-regular-svg-icons/faThumbsUp'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'


library.add(faShoePrints, faBars, faSearch, faShoppingCart, faSignInAlt, faUserPlus,
            faCommentAlt, faStore, faChevronDown, faThumbsUp, faBoxOpen, faAward,
            faTrashAlt, faMapMarkedAlt, faMobile, faEnvelopeOpenText, faFacebookSquare,
            faTwitterSquare, faInstagram, faAt, faLock, faLockOpen, faEye, faUser)

Vue.component('font-awesome-icon', FontAwesomeIcon)
